#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>
#include <fstream>
#include <bitset>

using namespace std;

#define foreach(it, c) for (__typeof__((c).begin()) it=(c).begin(); it != (c).end(); ++it)
template <typename T> void print_container(ostream& os, const T& c) { const char* _s = " "; if (!c.empty()) { __typeof__(c.begin()) last = --c.end(); foreach (it, c) { os << *it; if (it != last) os << _s; } } }
template <typename T> ostream& operator<<(ostream& os, const vector<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const set<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const multiset<T>& c) { print_container(os, c); return os; }
template <typename T> ostream& operator<<(ostream& os, const deque<T>& c) { print_container(os, c); return os; }
template <typename T, typename U> ostream& operator<<(ostream& os, const map<T, U>& c) { print_container(os, c); return os; }
template <typename T, typename U> ostream& operator<<(ostream& os, const pair<T, U>& p) { os << "(" << p.first << ", " << p.second << ")"; return os; }

template <typename T> void print(T a, int n, const string& split = " ") { for (int i = 0; i < n; i++) { cout << a[i]; if (i + 1 != n) cout << split; } cout << endl; }
template <typename T> void print2d(T a, int w, int h, int width = -1, int br = 0) { for (int i = 0; i < h; ++i) { for (int j = 0; j < w; ++j) { if (width != -1) cout.width(width); cout << a[i][j] << ' '; } cout << endl; } while (br--) cout << endl; }
template <typename T> void input(T& a, int n) { for (int i = 0; i < n; ++i) cin >> a[i]; }
#define dump(v) (cerr << #v << ": " << v << endl)

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define clr(a, x) memset(a, x, sizeof(a))
#define sz(a) ((int)(a).size())
#define mp(a, b) make_pair(a, b)
#define ten(n) ((long long)(1e##n))

template <typename T, typename U> void upmin(T& a, const U& b) { a = min<T>(a, b); }
template <typename T, typename U> void upmax(T& a, const U& b) { a = max<T>(a, b); }
template <typename T> void uniq(T& a) { sort(a.begin(), a.end()); a.erase(unique(a.begin(), a.end()), a.end()); }
template <class T> string to_s(const T& a) { ostringstream os; os << a; return os.str(); }
template <class T> T to_T(const string& s) { istringstream is(s); T res; is >> res; return res; }
void fast_io() { cin.tie(0); ios::sync_with_stdio(false); }
bool in_rect(int x, int y, int w, int h) { return 0 <= x && x < w && 0 <= y && y < h; }

typedef long long ll;
typedef pair<int, int> pint;

const int dx[] = { 0, 1, 0, -1 };
const int dy[] = { 1, 0, -1, 0 };


template <class T>
class Dinic
{
    struct DinicEdge
    {
        int to;
        T cap;
        int rev;
        DinicEdge(int to, T cap, int rev)
            : to(to), cap(cap), rev(rev) {}
        DinicEdge() { DinicEdge(0, 0, 0); }
    };


    void bfs(int s)
    {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        q.push(s);
        level[s] = 0;
        while (!q.empty())
        {
            int v = q.front(); q.pop();
            for (int i = 0; i < (int)edges[v].size(); ++i)
            {
                DinicEdge& e = edges[v][i];
                if (e.cap > 0 && level[e.to] == -1)
                {
                    level[e.to] = level[v] + 1;
                    q.push(e.to);
                }
            }
        }
    }

public:
    int V;
    vector<vector<DinicEdge> > edges;
    vector<int> level;
    vector<int> iter;

    Dinic(int V)
        : V(V), edges(V), level(V), iter(V) { }

    void add_edge(int from, int to, T cap)
    {
        edges[from].push_back(DinicEdge(to, cap, (int)edges[to].size()));
        edges[to].push_back(DinicEdge(from, 0, (int)(edges[from].size() - 1)));
    }
    void add_undirected(int from, int to, T cap)
    {
        edges[from].push_back(DinicEdge(to, cap, (int)edges[to].size()));
        edges[to].push_back(DinicEdge(from, cap, (int)(edges[from].size() - 1)));
    }
    // void add_undirected(int a, int b, T cap)
    // {
    //     add_edge(a, b, cap);
    //     add_edge(b, a, cap);
    // }

    T dfs(int v, int t, T f)
    {
        if (v == t)
            return f;

        for (int& i = iter[v]; i < (int)edges[v].size(); ++i)
        {
            DinicEdge& e = edges[v][i];
            if (e.cap > 0 && level[v] < level[e.to])
            {
                T d = dfs(e.to, t, min(f, e.cap));
                if (d > 0)
                {
                    e.cap -= d;
                    edges[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }

    T max_flow(int s, int t)
    {
        T flow = 0;
        for (;;)
        {
            bfs(s);
            if (level[t] == -1)
                break;

            fill(iter.begin(), iter.end(), 0);
            const T INF = (T)(1LL << 60) | (1 << 29);
            for (T f; (f = dfs(s, t, INF)) > 0; )
                flow += f;
        }
        return flow;
    }
};
int w, h, b;
int river(int x, int y, int io)
{
    return 2 + w * h * io + (y * w + x);
}
int main()
{
    int T;
    cin >> T;
    for (int C = 1; C <= T; ++C)
    {
        cin >> w >> h >> b;
        bool a[512][128];
        clr(a, 0);
        rep(i, b)
        {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            for (int y = y1; y <= y2; ++y)
                for (int x = x1; x <= x2; ++x)
                    a[y][x] = true;
        }

        const int in = 0, out = 1;
        int src = 0, sink = 1;
        Dinic<int> dinic(10 + 2 * w * h);
        rep(x, w)
        {
            dinic.add_edge(src, river(x, 0, in), 1);
            dinic.add_edge(river(x, h - 1, out), sink, 1);
        }
        rep(y, h) rep(x, w)
        {
            if (!a[y][x])
            {
                dinic.add_edge(river(x, y, in), river(x, y, out), 1);

                rep(dir, 4)
                {
                    int nx = x + dx[dir], ny = y + dy[dir];
                    if (in_rect(nx, ny, w, h) && !a[ny][nx])
                        dinic.add_edge(river(x, y, out), river(nx, ny, in), 1);
                }
            }
        }
        int flow = dinic.max_flow(src, sink);
        printf("Case #%d: %d\n", C, flow);
    }
}
