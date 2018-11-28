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

const int maxn = 20;
unordered_set<int64> ss[maxn];
int n; 

inline int bit(int k) { return 1 << k; }

int64 mhash(const string& word) {
    int64 res = 0;
    for (char c : word) {
        res *= 173;
        res += c;
        res %= int(1e9) + 7;
    }
    return res;
}

void parse(int id, const string& line) {
    //E(id); Eo(line);
    stringstream s(line);
    string word;
    while (s >> word) ss[id].insert(mhash(word));
}

int go(int mask) {
    vector<int64> left(ss[0].begin(), ss[0].end());
    //for (auto i : left) { Eo(i); }
    unordered_set<int64> right(ss[1].begin(), ss[1].end());
    for (int j = 0; j < n - 2; ++j)  {
        if (mask & bit(j))
            for (const auto& w : ss[j + 2]) left.push_back(w);
        else
            for (const auto& w : ss[j + 2]) right.insert(w);
    }
    int res = 0;
#if 1
    for (const auto& w : left) if (right.count(w)) {
        ++res;
        right.erase(w);
    }
#else
    if (Sz(left) < Sz(right)) {
        for (const auto& w : left) if (right.count(w)) ++res;
    } else {
        for (const auto& w : right) if (left.count(w)) ++res;
    }
#endif
    return res;
}

int main() {
#if 0
    for (int i = 0; i < 20; ++i) {
        int wc = (i < 2 ? 1000 : 10);
        for (int i = 0; i < wc; ++i) {
            for (int j = 0; j < 10; ++j) printf("%c", 'a' + (rand() % 26));
            printf(" ");
        }
        puts("");
    }
    return 0;
#endif
    ios_base::sync_with_stdio(false); cin.tie(0);
    int ts; cin >> ts;
    for (int test = 1; test <= ts; ++test) {
        E(test); Eo(ts);
        cin >> n;
        for (int i = 0; i < n; ++i) ss[i].clear();
        string s;
        getline(cin, s);
        for (int i = 0; i <  n; ++i) {
            getline(cin, s);
            parse(i, s);
        }
        int res = inf;
        const int to = bit(n - 2);
#pragma omp parallel for reduction(min:res)
        for (int i = 0; i < to; ++i) {
            int cur = go(i);
            res = min(res, cur);
        }
        cout << "Case #" << test << ": " << res << endl;
    }

    return 0;
}
