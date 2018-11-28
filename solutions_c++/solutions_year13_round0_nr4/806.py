//{ Template
using namespace std;
//{ C-headers
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <ctime>
#include<sstream>
//}
//{ C++-headers
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS DBL_EPSILON
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2 * acos (0.0)
//}
//}

int n , open[25] , keys[205];
vector<int>number_of_keys[25];
stack<int>stk;
int dp[1<<20 + 7 ];
int solve(int mask)
{
    if(__builtin_popcount(mask) == n ) return 1;
    if(dp[mask]!=-1) return dp[mask];
    rep(i,n)
    {
        if(mask&1<<i) continue;
        if(keys[ open[i] ])
        {
            keys[ open[i] ]--;
            forstl(it,number_of_keys[i]) keys[*it]++;
            if(solve(mask|1<<i))
            {
                stk.push(i);
                return dp[mask] = 1;
            }
            keys[open[i]]++;
            forstl(it,number_of_keys[i]) keys[*it]--;
        }
    }
    return dp[mask]=0;
}

void clear()
{
    memset(dp,-1,sizeof dp);
    memset(keys,0,sizeof keys);
    while(!stk.empty()) stk.pop();
    rep(i,21)number_of_keys[i].clear();
}

int main()
{
       // freopen("in.txt", "r", stdin);
   // freopen("out.txt", "w", stdout);
    int test , cs = 1 , k ;
    scanf("%d",&test);
    while(test--)
    {
        clear();
        scanf("%d %d",&k,&n);
        rep(i,k)
        {
            int x ;
            cin >> x ;
            keys[x]++;
        }
        rep(i,n)
        {
            cin >> open[i];
            int a ,b;
            scanf("%d",&a);
            rep(j,a)
            {
                scanf("%d",&b);
                number_of_keys[i].push_back(b);
            }
        }
        printf("Case #%d:",cs++);
        if(solve(0))
        {

            while(!stk.empty())
            {
                printf(" %d",stk.top()+1);
                stk.pop();
            }
        }
        else printf(" IMPOSSIBLE");
        puts("");
    }
    return 0 ;
}
