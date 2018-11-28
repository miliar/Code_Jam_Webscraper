#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<map>
#include<algorithm>
#include<limits.h>
#include<set>
#include<math.h>
 
using namespace std;
#define lli long long int
#define ulli unsigned long long int
#define in(t) scanf("%d",&t)
#define inlf(t) scanf("%lf",&t)
#define inl(t) scanf("%ld",&t)
#define inll(t) scanf("%lld",&t)
#define inlu(t) scanf("%llu",&t)
#define MOD 1000000007

int main()
{
    
    #ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    #endif
    
    int t,cases;
    double c,f,x,time1,time2,sum,inc;
    in(t);
    for(cases=1;cases<=t;cases++)
    {
    sum=time1=time2=0;
    inc=2;
    inlf(c);
    inlf(f);
    inlf(x);
    while(1)
    {
    time1=x/inc;
    time2=c/inc + x/(f+inc);
    if(time1>time2)
    {
    sum+=c/inc;
    inc+=f;
    }
    else
    {
    sum+=x/inc;
    break;
    }
    }
    printf("Case #%d: %.7lf\n",cases,sum);
    }
    return 0;
}
