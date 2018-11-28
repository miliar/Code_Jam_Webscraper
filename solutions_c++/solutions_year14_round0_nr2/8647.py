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
#include <unistd.h>
#include <stdint.h>

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

#define Sd(t)   scanf("%d",&t)
#define Slld(t) scanf("%lld",&t)
#define Ss(t)   scanf("%s",t)
#define Slf(t)  scanf("%lf",&t)

#define Pd(t)   printf("%d",t)
#define Plld(t) printf("%lld",t)
#define Ps(t)   printf("%s",t)
#define Plf(t)  printf("%lf",t)

#define Pc(t)    printf("%c",t)
#define Pn       printf("\n")
#define MOD 1000000007
#define MX 10000

using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, presentCookies;
    double c,f,x;
    Sd(T);
    double timePerCookie;
    REP(cs,T){
        double time = 0;
        presentCookies = 0;

        double cookiesPerSecond = 2;
        timePerCookie = 1 / cookiesPerSecond;
        scanf("%lf %lf %lf",&c,&f,&x);
        while(presentCookies < x){
            double time1 = (c)*(1/cookiesPerSecond) + (x)*(1/(cookiesPerSecond+f));
            double time2 = (x)*(1/cookiesPerSecond);
            //cout<<"tm1 "<<time1<< " tm2 "<<time2<<"\n";
            if(time1 < time2){
                //cout<<"Buying farm\n";
                time += time1 - (x)*(1/(cookiesPerSecond+f));
                cookiesPerSecond += f;
            }
            else{
                //cout<<"Breaking out\n";
                time += time2;
                break;
            }
        }
        printf("Case #%d: %0.7lf\n",cs+1,time);
    }
    return 0;
}
