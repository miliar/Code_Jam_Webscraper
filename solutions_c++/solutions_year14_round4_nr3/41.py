#include <bits/stdc++.h>

using namespace std;

#define long int64_t

#define rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=a;i<(b);++i)
#define all(u) begin(u),end(u)
#define rall(u) (u).rbegin(),(u).rend()
#define uniq(u) (u).erase(unique(all(u)),end(u))

#define mp make_pair
#define pb push_back
#define eb emplace_back

inline long distint(long a, long b, long c, long d)
{
    if (b < c) return c - b - 1;
    if (d < a) return a - d - 1;
    return 0;
}

struct rect
{
    long ax, ay, bx, by;
    rect(long ax, long ay, long bx, long by) : ax(ax), ay(ay), bx(bx), by(by) {}
    long dist(const rect& t) {
        return max(distint(ax, bx, t.ax, t.bx), distint(ay, by, t.ay, t.by));
    }
};

ostream& operator <<(ostream& out, const rect& t)
{
    return out << t.ax << ',' << t.ay << ',' << t.bx << ',' << t.by;
}

long w, h, b;
vector<rect> rects;

void input()
{
    rects.clear();

    cin >> w >> h >> b;
    rects.eb(-1, 0, -1, h - 1);
    rep(i, b) {
        long ax, ay, bx, by;
        cin >> ax >> ay >> bx >> by;
        rects.eb(ax, ay, bx, by);
    }
    rects.eb(w, 0, w, h - 1);
}

vector<long> d;

struct node
{
    int v;
    node(int v) : v(v) {}
    bool operator <(const node& t) const {
        return d[v] > d[t.v];
    }
};

long solve()
{
    const int V = rects.size();

    d.assign(V, long(1e12));

    priority_queue<node> q;
    d[0] = 0, q.push(0);
    while (not q.empty()) {
        int v = q.top().v;
        q.pop();

        if (v == V - 1) {
            return d[v];
        }

        rep(nv, V) {
            long nd = d[v] + rects[v].dist(rects[nv]);
            if (nd < d[nv]) {
                d[nv] = nd, q.push(nv);
            }
        }
    }

    return -1;
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int T, cnt = 0;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << ++cnt << ": ";
        input();
        cout << solve() << endl;
    }

    return 0;
}
