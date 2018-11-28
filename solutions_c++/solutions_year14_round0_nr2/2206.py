#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>
#define MOD 1000000007
using namespace std;
int main()
{
    int t,n,ctr=0;
    double c,f,x,t1,t2,t3,ans,rate;
    freopen("jam14i.txt","r",stdin);
    freopen("jam14o.txt","w",stdout);
    scanf("%d",&t);

    while(t--)
    {
        ctr++;
        scanf("%lf %lf %lf",&c,&f,&x);
        ans = 0.00;
        rate = 2.00;
        while(1)
        {
            t1 = x/rate;
            t2 = c/rate;
            t3 = x/(rate+f);

            if( (t2+t3) < t1)
            {
                ans += (t2);
                rate += f;
            }
            else
            {
                ans += t1;
                break;
            }

            //printf("ans=%.7lf rate=%.7lf t1=%.7lf t2=%.7lf t3=%.7lf\n",ans,rate,t1,t2,t3);
        }

        printf("Case #%d: %.7lf\n",ctr,ans);
    }
    return 0;
}
