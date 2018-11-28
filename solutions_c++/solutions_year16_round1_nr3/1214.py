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

/* check if a key is in container C */
template <class C>
inline bool in_(const typename C::key_type& k, const C& A)
{ return A.find(k) != A.end(); }

/* gcj 2016 1a C */

const int maxn = 1e3+5;
int F[maxn][maxn];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int t=0,T; cin >> T;
    while (T--) {
        memset(F,0,sizeof(F));
        int N; cin >> N;
        FOR(i,0,N) {
            int j; cin >> j; j--;
            F[i][j] = 1;
        }
        VI A;
        int ans = 0;
        FOR(mask,0,1<<N) {
            A.clear();
            FOR(i,0,N) if (mask & (1<<i)) {
                A.push_back(i);
            }
            sort(ALL(A));
            do {
                const int x = A.size();
                bool good = true;
                FOR(i,0,x) {
                    const int u = A[i];
                    const int v = A[(i+1)%x];
                    const int w = A[(i-1+x)%x];
                    good &= (F[u][v] || F[u][w]);
                }
                if (good)
                    ans = max(ans,x);
            } while (next_permutation(ALL(A)));
        }
        printf("Case #%d: %d\n",++t,ans);
    }
    return 0;    
}
