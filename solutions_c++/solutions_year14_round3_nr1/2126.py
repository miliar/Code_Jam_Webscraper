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

const int inf = 0x3f3f3f3f;
const int maxv = 1100;

int gcd(int a,int b)
{
    if (b == 0)
        return a;
    return gcd(b,a%b);
}
int lcm(int a,int b)
{
    LL ans = (LL)a*b/gcd(a,b);
    return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
    //freopen("foo", "rt", stdin);
#endif
    int T,case_=1; scanf("%d",&T);
    while (T--) {
        char ans[256] = "impossible";
        LL p,q; scanf("%lld/%lld",&p,&q);
        int g = gcd(p,q);
        p /= g;
        q /= g;
        LL A = 1;
        bool valid = false;
        while (A < q && valid == false) {
            A *= 2;
            if (A == q) 
                valid = true;
        }
        if (valid && p <= q && q % 2 == 0) {
            int i = 0;
            for (; i < 41; i++) {
                if (p >= q)
                    break;
                q /= 2;
            }
            if (i < 41)
                sprintf(ans,"%d",i);

        }
        printf("case #%d: %s\n",case_,ans);
        //fprintf(stderr, "case #%d: %d\n",case_,ans);
        case_++;
    }
    return 0;
}
