#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
//#include <regex>

/* g++ -g -std=c++0x */
/* g++ -g -std=c++11 */

using namespace std;

// std::ios::sync_with_stdio(false);

// freopen("input.txt", "rt", stdin);
// freopen("output.txt", "wt", stdout);

#define ALL(c)          (c).begin(), (c).end()
#define ALLR(c)         (c).rbegin(), (c).rend()
#define FOR(i,a,b)      for (__typeof(a) i=(a); i < (b); ++i)
#define FORR(i,a,b)     for (__typeof(a) i=(a); i > (b); --i)
#define FOR_ALL(i,c)    for (__typeof((c).begin()) i=(c).begin();   \
                             i != (c).end(); ++i)
#define FOR_ALLR(i,c)   for (__typeof((c).rbegin()) i=(c).rbegin(); \
                             i != (c).rend(); ++i)
#define SZ(array)       (sizeof(array)/sizeof(array[0]))
#define lc(x)           (x<<1)     /* 2*x */
#define rc(x)           (x<<1 | 1) /* 2*x+1 */
#define lowbit(x)       (x & (-x)) /* 0b10100 -> 0b100 */

typedef long long       LL;
typedef map<int,int>    MII;
typedef pair<int,int>   PII;
typedef set<int>        SI;
typedef vector<bool>    VB;
typedef vector<double>  VD;
typedef vector<int>     VI;
typedef vector<string>  VS;
typedef pair<int,char>  PIC;

/* check if a key is in container C */
template <class C>
inline bool in_(const typename C::key_type& k, const C& A)
{ return A.find(k) != A.end(); }

LL gcd(const LL a, const LL b)
{ return b == 0 ? a : gcd(b,a%b); }


inline string i2str(LL i)
{ ostringstream os; os << i; return os.str(); }

/* inline string i2str(LL i) */
/* { return std::to_string(i); }   /\* c++0x *\/ */

inline LL str2i(const string& s)
{ LL i; stringstream(s) >> i; return i; }


const int maxn = 1e6;
string ans[maxn];
int t;
bool dfs(const int d, vector<PIC> A)
{
    sort(ALL(A));
    int total = 0;
    const int n = A.size();
    FOR(i,0,n) {
        total += A[i].first;
    }
    if (total == 0) {
        printf("Case #%d: ",++t);
        FOR(i,0,d)
            printf("%s ",ans[i].c_str());
        printf("\n");
        return true;
    }
    const int maxx = A[n-1].first;
    if (maxx > total/2)
        return false;
    {
        ans[d] = string(1,A[n-1].second);
        vector<PIC> B;
        FOR(i,0,n) if (A[i].first) {
            if (i == n-1)
                B.push_back(PIC(A[i].first-1,A[i].second));
            else
                B.push_back(A[i]);
        }
        if (dfs(d+1,B))
            return true;
    }
    if (A[n-1].first > 1) {
        ans[d] = string(1,A[n-1].second) + string(1,A[n-1].second);
        vector<PIC> B;
        FOR(i,0,n) if (A[i].first) {
            if (i == n-1)
                B.push_back(PIC(A[i].first-2,A[i].second));
            else
                B.push_back(A[i]);
        }
        if (dfs(d+1,B))
            return true;
    }
    if (n > 1) {
        ans[d] = string(1,A[n-1].second) + string(1,A[n-2].second);
        vector<PIC> B;
        FOR(i,0,n) if (A[i].first) {
            if (i == n-2 || i == n-1)
                B.push_back(PIC(A[i].first-1,A[i].second));
            else
                B.push_back(A[i]);
        }
        if (dfs(d+1,B))
            return true;
    }
    return false;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int T; scanf("%d",&T);
    t = 0;
    while (T--) {
        int N; cin >> N;
        vector<pair<int,char>> A;
        FOR(i,0,N) {
            int cnt; cin >> cnt;
            A.push_back(PIC(cnt,i+'A'));
        }
        dfs(0,A);
    }
    exit(0);
}
