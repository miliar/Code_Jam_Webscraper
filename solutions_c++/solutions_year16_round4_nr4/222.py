// @author cebrusfs
// headers {{{
#include<bits/stdc++.h>
using namespace std;
// }}}
// macros {{{
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define UNIQUE(x) (sort(ALL(x)), ((x).erase(unique(ALL(x)), (x).end())))
#define MSA(x, v) std::fill(ALL(x), (v))
#define MS(st, ed, v) std::fill((st), (ed), (v))

#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)

#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

typedef pair<int, int> PII;
#define MP make_pair
#define F first
#define S second

typedef vector<int> VI;
#define PB push_back
#define PF push_front

#define PPB pop_back
#define PPF pop_front

#define runtime() ((double)clock() / CLOCKS_PER_SEC)

const double eps = 1e-7;

// C++11
#if __cplusplus >= 201103L
#define MT make_tuple
typedef tuple<int, int> TII;

// dump() {{{
template<typename T>
void _dump(const char* s, T&& head) {
    cerr<< s << "=" << head << endl;
}

template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c = 0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{') c++;
        if (*s==')' || *s==']' || *s=='}') c--;
        cerr << *s++;
    }
    cerr << "=" << head << ", ";
    _dump(s+1, tail...);
}

#ifdef FISH
#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, __VA_ARGS__); \
} while (0);
#else
#define dump(...) ;
#endif

template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s << "[";
    for (auto it = b; it != e; it++) s << (it == b ? "":" ") << *it;
    s << "]";
    return s;
}

template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) { return s<<"("<<p.first<<","<<p.second<<")"; }
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<(ostream &s, const set<T> &c) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<(ostream &s, const unordered_set<T> &c) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const map<A,B> &c) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const unordered_map<A,B> &c) { return _out(s,ALL(c)); }
// }}}

#endif
// }}}

#define MAX 5

char mp[MAX][MAX];
int ord[MAX];
bool used[MAX];

bool dfs(int n, int d, bool a[MAX][MAX])
{
    if (d == n)
    {
        for (int i = 0; i < n; ++i)
            if (not used[i]) return false;
        return true;
    }

    int idx = ord[d];

    bool checked = false;
    for (int i = 0; i < n; ++i)
    {
        if (a[idx][i] and not used[i])
        {
            used[i] = true;
            bool res = dfs(n, d + 1, a);
            used[i] = false;
            if (not res) return false;
            checked = true;
        }
    }
    return checked;
}

bool solve(int n, bool a[MAX][MAX])
{
    for (int i = 0; i < n; ++i)
        ord[i] = i, used[i] = false;

    do {
        bool res = dfs(n, 0, a);
        if (not res) return false;
    } while (next_permutation(ord, ord + n));
    return true;
}
bool a[MAX][MAX];
int main()
{
    int z;
    scanf("%d", &z);
    for (int zi = 1; zi <= z; ++zi)
    {
        int n;
        scanf("%d", &n);

        for (int i = 0; i < n; ++i)
            scanf("%s", mp[i]);

        int N = n * n;

        int ans = N;
        for (int k = 0; k < (1 << N); ++k)
        {
            int cost = 0;
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                {
                    int v = k & (1 << (i * n + j));
                    a[i][j] = mp[i][j] == '1' or v;
                    if (v) cost += 1;
                }

            bool res = solve(n, a);
            if (res) ans = min(cost, ans);
        }
        printf("Case #%d: %d\n", zi, ans);
    }
}

