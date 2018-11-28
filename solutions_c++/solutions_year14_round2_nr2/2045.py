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
//#include <tr1/memory>

/* compilation flags: */
/* g++ -g -std=c++0x google_codejam_T.cpp */
/* g++ -g -std=c++11 google_codejam_T.cpp */

using namespace std;
//using namespace std::tr1;

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
typedef set<int>        SI;
typedef vector<int>     VI;
typedef vector<string>  VS;
typedef pair<int,int>   PII;

// typedef shared_ptr<VI>  VI_ptr;
// typedef shared_ptr<SI>  SI_ptr;

const long inf = LONG_MAX;      // 2147483647 (2^31-1) or greater
const long ninf = LONG_MIN;     // -2147483647 (-2^31+1) or less

int main()
{
    int T,case_=1; scanf("%d",&T);
    while (T--) {
        int A,B,K; scanf("%d%d%d",&A,&B,&K);
        set<PII> P;
        FOR(a,0,A) FOR(b,0,B) {
            if ((a & b) < K) {
                P.insert(PII(a,b));
            }   
        }
        LL ans = P.size();
        printf("case #%lld: %d\n",case_,ans);
        //fprintf(stderr, "case #%d: %d\n",case_,ans);
        case_++;
    }
    
    return 0;
}
