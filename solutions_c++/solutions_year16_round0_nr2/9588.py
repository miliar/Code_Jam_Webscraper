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

constexpr inline int bit(int t) { return 1 << t; }

random_device rdev; mt19937 rmt(rdev()); uniform_int_distribution<> rnd(0, 0x7fffffff);
inline int mrand(int mod = 0x7fffffff) { return rnd(rmt) % mod; }

const int maxn = 10;

int dp[bit(maxn)];

int tos(string s) {
    int res = 0;
    reverse(All(s));
    for (char c : s) {
        res *= 2;
        if (c == '-')
            ++res;
    }
    return res;
}

string frs(int num) {
    string s;
    while (num) {
        if (num % 2 == 0)
            s += '+';
        else
            s += '-';
        num /= 2;
    }
    while (Sz(s) < maxn)
        s += '+';
    return s;
}

int go(int ii) {
    int& res = dp[ii];
    if (res == inf) {
        res = inf - 1;
        const string s = frs(ii);
        for (int i = 1; i <= Sz(s); ++i) {
            string t = s.substr(0, i);
            reverse(All(t));
            for (char& c : t)
                if (c == '-')
                    c = '+';
                else
                    c = '-';
            t += s.substr(i);
            assert(Sz(t) <= 10);
            const int to = tos(t);
            res = min(res, go(to) + 1);
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);

    memset(dp, 0x3f, sizeof(dp));
    dp[0] = 0;
    vector<int> que(1, 0);
    for (int id = 0; id < Sz(que); ++id) {
        int ii = que[id];
        EO(ii);
        const string s = frs(ii);
        for (int i = 1; i <= Sz(s); ++i) {
            string t = s.substr(0, i);
            reverse(All(t));
            for (char& c : t)
                if (c == '-')
                    c = '+';
                else
                    c = '-';
            t += s.substr(i);
            const int to = tos(t);
            if (dp[to] == inf) {
                dp[to] = dp[ii] + 1;
                que.push_back(to);
            }
        }
    }

    int T; cin >> T;
    for (int test = 1; test <= T; ++test) {
        string s; cin >> s;
        int a = tos(s);
        cout << "Case #" << test << ": " << dp[a] << endl;
    }

    return 0;
}
