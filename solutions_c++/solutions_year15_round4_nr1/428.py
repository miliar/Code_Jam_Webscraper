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
const int dir[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

random_device rdev; mt19937 rmt(rdev()); uniform_int_distribution<> rnd(0, 0x7fffffff);
inline int mrand(int mod = 0x7fffffff) { return rnd(rmt) % mod; }

const int maxn = 111;
string f[maxn];
int r, c;
bool visit[maxn][maxn];

int getdir(char cc, int lastd) {
    switch(cc) {
        case '^': return 3;
        case 'v': return 1;
        case '<': return 2;
        case '>': return 0;
    }
    return lastd;
}

int go() {
    int res = 0;
    for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) if (f[i][j] != '.') {
        E("========="); E(i); Eo(j);
        memset(visit, 0, sizeof(visit));
        bool goout = false;
        int ci = i, cj = j, d = getdir(f[i][j], -1);
        int startd = d;
        bool changed = false;
        while (!visit[ci][cj]) {
            visit[ci][cj] = true;
            ci += dir[d][0];
            cj += dir[d][1];
            if (ci < 0 || ci == r || cj < 0 || cj == c) {
                E(d); E(ci); Eo(cj);
                goout = true;
                break;
            }
            d = getdir(f[ci][cj], d);
            if (f[ci][cj] != '.') changed = true;
        }
        if (!goout) continue;
        if (changed) continue;
        Eo("here");
        bool ok = false;
        for (int k = 0; !ok && k < 4; ++k) {
            ci = i, cj = j;
            while (0 <= ci && ci < r && 0 <= cj && cj < c) {
                if ((ci != i || cj != j) && f[ci][cj] != '.') {
                    ok = true;
                    break;
                }
                ci += dir[k][0];
                cj += dir[k][1];
            }
        }
        if (!ok) return -1;
        ++res;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    int ts; cin >> ts;
    for (int test = 1; test <= ts; ++test) {
        cin >> r >> c;
        for (int i = 0; i < r; ++i) cin >> f[i];
        int res = go();
        cout << "Case #" << test << ": " << (res == -1 ? "IMPOSSIBLE" : to_string(res)) << endl;
    }

    return 0;
}
