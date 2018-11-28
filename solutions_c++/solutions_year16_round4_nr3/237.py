#include <bits/stdc++.h>
using namespace std;

#ifdef ILIKEGENTOO
#   define Eo(x) { cerr << #x << " = " << (x) << endl; }
#   define E(x) { cerr << #x << " = " << (x) << "   "; }
#   define FREOPEN(x)
#else
#   define Eo(x) {}
#   define E(x) {}
#   define FREOPEN(x) (void)freopen(x ".in", "r", stdin);(void)freopen(x ".out", "w", stdout);
#endif
#define EO(x) Eo(x)
#define Sz(x) (int((x).size()))
#define All(x) (x).begin(),(x).end()

template<class A, class B> ostream &operator<<(ostream &os, const pair<A, B>& p) { return os << '(' << p.first << ", " << p.second << ')'; }

template<class C> void operator<<(vector<C> &v, const C &x){v.push_back(x);}
template<class D> void operator>>(vector<D> &v, D &x){assert(!v.empty()); x=v.back(); v.pop_back();}
template<class E> void operator<<(set<E> &v, const E &x){v.insert(x);}

typedef double flt;
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;

const int inf = 0x3f3f3f3f;
const int64 inf64 = 0x3f3f3f3f3f3f3f3fLL;
const flt eps = 1e-8;
const flt pi = acos(-1.0);
const int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

constexpr inline int bit(int t) { return 1 << t; }

random_device rdev; mt19937 rmt(rdev()); uniform_int_distribution<> rnd(0, 0x7fffffff);
inline int mrand(int mod = 0x7fffffff) { return rnd(rmt) % mod; }

const int maxr = 18, maxc = 18;

int id[maxr][maxc][4];

struct Pos {
    int row, col, sec;

    bool upd(int qid) {
        if (id[row][col][sec] == qid)
            return false;
        //E(row); E(col); E(sec); Eo(qid);
        id[row][col][sec] = qid;
        return true;
    }
};

vector<pii> bfs(int r, int c, int mask) {
    vector<pii> res;
    memset(id, 0xc0, sizeof(id));

    int lastid = 1;

    auto go = [&](Pos pos) -> int {
        queue<Pos> que;
        que.push(pos);
        pos.upd(lastid);
        while (!que.empty()) {
            pos = que.front();
            que.pop();

            // near sectors
            {
                int nid = 0;
                const int maskid = pos.row * c + pos.col;
                if (mask & bit(maskid)) {
                    switch (pos.sec) {
                        case 0: nid = 3; break;
                        case 1: nid = 2; break;
                        case 2: nid = 1; break;
                        case 3: nid = 0; break;
                    }
                } else {
                    switch (pos.sec) {
                        case 0: nid = 1; break;
                        case 1: nid = 0; break;
                        case 2: nid = 3; break;
                        case 3: nid = 2; break;
                    }
                }

                Pos npos(pos);
                npos.sec = nid;
                if (npos.upd(lastid))
                    que.push(npos);
            }

            // near cells
            for (int k = 0; k < 4; ++k) {
                if (k != pos.sec) continue;
                Pos npos(pos);
                npos.row += dir[k][0];
                npos.col += dir[k][1];
                if (npos.row < 0 || npos.row >= r || npos.col < 0 || npos.col >= c) continue;
                npos.sec = (npos.sec + 2) % 4;
                if (npos.upd(lastid))
                    que.push(npos);
            }
        }

        return ++lastid;
    };

    unordered_map<int, vector<int>> ans;

    for (int i = 0; i < c; ++i) {
        for (int j = 0; j < 2; ++j) {
            int sec = (j == 0 ? 0 : 2);
            int row = 0 + j * (r-1);
            int col = i;
            if (id[row][col][sec] < 0) 
                go(Pos{row, col, sec});

            int tasknum = 0;
            if (j == 0)
                tasknum = 1 + i;
            else
                tasknum = r + c + (c - i);
            ans[id[row][col][sec]].push_back(tasknum);
        }
    }
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < 2; ++j) {
            int sec = (j == 0 ? 3 : 1);
            int row = i;
            int col = 0 + j * (c-1);
            if (id[row][col][sec] < 0) {
                go(Pos{row, col, sec});
            }

            int tasknum = 0;
            if (j == 0)
                tasknum = 2 * c + r + (r - i);
            else
                tasknum = c + 1 + i;
            ans[id[row][col][sec]].push_back(tasknum);
        }
    }

    for (const auto& i : ans) {
        if (i.second.size() != 2)
            return vector<pii>();
        int a = i.second.front();
        int b = i.second.back();
        res.push_back(pii(min(a, b), max(a, b)));
    }
    sort(All(res));

    return res;
}

void print(vector<pii>& v) {
    Eo("=== begin ===");
    for (pii i : v) {
        Eo(i);
    }
    Eo("=== end ===");
}

int main() {
    // FREOPEN("c");
    ios_base::sync_with_stdio(false); cin.tie(0);

#if 0
    auto paris = bfs(1, 2, 0);
    for (auto i : paris) {
        Eo(i);
    }
    return 0;
#endif

    int tests; cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int r, c; cin >> r >> c;

        vector<pii> req;
        for (int i = 0; i < 2*(r+c); i += 2) {
            int a, b; cin >> a >> b;
            req.push_back(pii(min(a,b), max(a,b)));
        }
        sort(All(req));

        //print(req);

        vector<pii> res;
        cout << "Case #" << test << ":" << "\n";
        for (int i = 0; i < bit(r * c); ++i) {
            res = bfs(r, c, i);
            //print(res);
            if (res == req) {
                for (int j = 0; j < r; ++j) {
                    for (int k = 0; k < c; ++k)
                        cout << ((i&bit(j*c+k)) ? '/' : '\\');
                    cout << '\n';
                }
                break;
            }
            res.clear();
        }


        if (res.empty())
            cout << "IMPOSSIBLE\n";
    }

    return 0;
}
