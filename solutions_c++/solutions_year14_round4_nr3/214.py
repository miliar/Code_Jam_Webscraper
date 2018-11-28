#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <array>
#include <map>

using namespace std;

#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

template <typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template <typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template <typename T> inline int sz(const T& x) { return (int) x.size(); }

const double PI = 2 * acos(0);

struct PT {
    int x, y;
    PT(int x = 0, int y = 0)
        : x(x), y(y) { }
};

const int INF = 1000000000;

struct Event {
    int l, r;
    char c;

    Event(int l, int r, char c)
        : l(l), r(r), c(c) { }

};

struct Arc {
    int dest;
    int cap;
    int next;
};

vector<int> head, dhead;
std::vector<Arc> arcs;
vector<int> dist, q, level, from;

int S, T;


istream& operator>>(istream& istr, PT& p) {
    return istr >> p.x >> p.y;
}

void add_arc(int u, int v, int c) {
    arcs.push_back({v, c, head[u]});
    head[u] = sz(arcs) - 1;
    arcs.push_back({u, 0, head[v]});
    head[v] = sz(arcs) - 1;
}

void connect(int u, int v) {
    add_arc(2 * u + 1, 2 * v + 0, 1);
    add_arc(2 * v + 1, 2 * u + 0, 1);
}


bool bfs() {
  fill(all(level), -1);
  int qt = 0, qh = 0;
  q[qt++] = S;
  level[S] = 0;
  while (qh != qt) {
    int u = q[qh++];
    // debug(u);
    if (u == T) return true;
    for (int arc = head[u]; arc != -1; arc = arcs[arc].next) {
      int v = arcs[arc].dest;
      if (arcs[arc].cap > 0 && level[v] == -1) {
        q[qt++] = v;
        level[v] = level[u] + 1;
      }
    }
  }
  return level[T] != -1;
}

int dfs(int v, int f, int pushed = 0) {
  if (v == T || f == 0) return f;
  for (int& arc = dhead[v]; arc != -1; arc = arcs[arc].next) {
    int to = arcs[arc].dest;
    if ((level[v] + 1 == level[to]) && (arcs[arc].cap > 0)) {
      int p = dfs(to, min(arcs[arc].cap, f));
      if (p > 0) {
        arcs[arc].cap -= p, arcs[arc ^ 1].cap += p;
        pushed += p, f -= p;
        if (f == 0) {
          return pushed;
        }
      }
    }
  }
  return pushed;
}

int main() {
    freopen("C-small-attempt1.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    // freopen("in.txt", "r", stdin);

    int nTests;
    cin >> nTests;

    // nTests = 2;
    forn (iTest, nTests) {

        int w, h, b;
        cin >> w >> h >> b;

        map<int, vector<Event> > events;

        vector<pair<PT, PT> > bld(b);
        forn (i, b) {
            cin >> bld[i].first >> bld[i].second;
            events[bld[i].first.y].emplace_back(bld[i].first.x, bld[i].second.x, '+');
            events[bld[i].second.y + 1].emplace_back(bld[i].first.x, bld[i].second.x, '-');
        }

        vector<vector<int> > grid;


        for (int i = 0; i < h; ++i)
            events[i];
        // events[0];
        // events[h - 1];

        vector<int> last(w, 0);
        for (auto& curr : events) {
            if (curr.first == h) break;
            // debug(curr.first);
            for (Event e : curr.second) {
                // debug(e.l);
                // debug(e.r);
                int d = (e.c == '+' ? +1 : -1);
                for (int x = e.l; x <= e.r; ++x) {
                    last[x] += d;
                }
            }
            grid.push_back(last);
        }

        int nodes = 2 * (grid.size() * w) + 2;

        S = nodes - 2;
        T = nodes - 1;

        q.resize(nodes);
        
        head.assign(nodes, -1);

        dist.resize(nodes);
        dhead.resize(nodes);
        level.resize(nodes);
        from.resize(nodes);
        arcs.resize(0);

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < w; ++j) {
                // cout << grid[i][j];
                if (grid[i][j]) continue;

                if (i == 0) add_arc(S, 2 * (i * w + j) + 0, 1);

                if (i + 1 < sz(grid) && !grid[i + 1][j]) {
                    connect(i * w + j, (i + 1) * w + j);
                }
                if (j + 1 < w && !grid[i][j + 1]) {
                    connect(i * w + j, i * w + (j + 1));
                }

                add_arc(2 * (i * w + j) + 0, 2 * (i * w + j) + 1, 1);

                if (i + 1 == sz(grid)) add_arc(2 * (i * w + j) + 1, T, 1);

            }
            // cout << endl;
        }

        // debug(w);

        // debug(sz(arcs));

        int flow = 0, pushed = 0;
        while (bfs()) {
            dhead = head;
            while ((pushed = dfs(S, INF)) > 0) {
                flow += pushed;
            }
        }
        cout << "Case #" << iTest + 1 << ": ";
        cout << flow << endl;
    }
    return 0;
}