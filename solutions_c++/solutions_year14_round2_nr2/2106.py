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
    freopen("B-small-attempt0 (2).in","r",stdin);
    freopen("B-small-attempt0 (2).out","w",stdout);
    #endif
    
    int a,b,k,t,cases,ans,i,j,f;
    in(t);
    for(cases=1;cases<=t;cases++)
    {
    ans=f=0;
    in(a);
    in(b);
    in(k);
    for(i=0;i<a;i++)
    {
    for(j=0;j<b;j++)
    {
    if((i&j)<k)
    ans++;
    }
    }
    printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
