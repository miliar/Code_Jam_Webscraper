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

double a[1001],b[1001];

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    #endif
    
    
    int t,cases,i,c,n,ans1,ans2;
    in(t);
    for(cases=1;cases<=t;cases++)
    {
    ans1=ans2=c=0;
    in(n);
    //double a[n+1],b[n+1];
    for(i=0;i<n;i++)
    inlf(a[i]);
    for(i=0;i<n;i++)
    inlf(b[i]);
    
    sort(a,a+n);
    sort(b,b+n);
    
    for(i=0;i<n;i++)
    {
    if(a[c]<b[i])
    c++;
    else
    ans2++;
    }
    c=0;
    if(n==1)
    {
    if(a[0]>b[0])
    ans1++;
    }
    else
    {
    for(i=0;i<n;i++)
    {
    if(a[i]>=b[c])
    {
    c++;
    ans1++;
    }
    }
    }
    printf("Case #%d: %d %d\n",cases,ans1,ans2);
    }
    return 0;
}
    
    
