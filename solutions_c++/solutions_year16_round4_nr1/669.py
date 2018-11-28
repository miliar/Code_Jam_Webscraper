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

char getwin(char a, char b) {
    assert(a != b);
    if (a == 'R') {
        return b == 'P' ? 'P' : 'R';
    } else if (a == 'S') {
        return b = 'R' ? 'R' : 'S';
    } else {
        return b == 'S' ? 'S' : 'P';
    }
}

bool go(string s) {
    while (Sz(s) > 1) {
        string t = "";
        for (int i = 0; i < Sz(s); i += 2) {
            if (s[i] == s[i + 1]) return false;
            t += getwin(s[i], s[i + 1]);
        }
        s = t;
    }
    return true;
}

string solveShuffle(int r, int p, int s) {
    string q = "";
    for (int i = 0; i < r; ++i) q += "R";
    for (int i = 0; i < p; ++i) q += "P";
    for (int i = 0; i < s; ++i) q += "S";

    sort(All(q));
    string best = "ZZRR";
    do {
        if (go(q) && q < best)
            best = q;
    }
    while (next_permutation(All(q)));
    
    if (!go(best))
        best = "IMPOSSIBLE";
    return best;
}


int main() {
    // FREOPEN("a");
    ios_base::sync_with_stdio(false); cin.tie(0);

    int tests; cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, r, p, s; cin >> n >> r >> p >> s;

        string res = "IMPOSSIBLE";
        string code = "RPS";
        for (int i = 0; i < 3; ++i) {
            int ary[3] = {r, p, s};
            if (ary[i] == 0) continue;
            string prev(1, code[i]);
            --ary[i];

            for (int j = 0; j < n; ++j)  {
                string next;
                for (char c : prev) {
                    int id = find(All(code), c) - code.begin();
                    int req = (id + 2) % 3;
                    ary[req]--;
                    next += min(code[id], code[req]);
                    next += max(code[req], code[id]);
                }
                prev = next;
            }

            bool ok = true;
            for (int j = 0; j < 3; ++j) if (ary[j] < 0) ok = false;

            for (int i = 1; i <= n; ++i) {
                string q = "";
                for (int j = 0; j < bit(n); j += bit(i)) {
                    string a = prev.substr(j, bit(i - 1));
                    string b = prev.substr(j + bit(i-1), bit(i-1));
                    q += min(a, b);
                    q += max(a, b);
                }
                prev = q;
            }

#if 0
            vector<string> ss;
            for (int i = 0; i < Sz(prev); i += 2)  {
                string qq = prev.substr(i, 2);
                sort(All(qq));
                ss.push_back(qq);
            }
            sort(All(ss));

            prev = "";
            for (string i : ss)
                prev += i;
#endif

            if (ok && (res == "IMPOSSIBLE" || prev < res))
                res = prev;
        }

        //string shfl = solveShuffle(r, p, s);
        cout << "Case #" << test << ": " << res << endl;
        //cout << shfl << endl;
        //E(res); Eo(shfl);
        //assert(shfl == res);
        
    }

    return 0;
}
