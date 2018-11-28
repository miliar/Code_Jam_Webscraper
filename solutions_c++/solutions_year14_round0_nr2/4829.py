#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
#include<stdlib.h>
#include<algorithm>
#define i_n(a) scanf("%d",&a)
#define l_n(a) scanf("%I64d",&a)
#define LL long long int
#define pb(a) push_back(a)
#define i_p(a) printf("%d\n",a)
#define l_p(a) printf("%I64d\n",a)
#include<limits.h>

using namespace std;
int maximum(int a,int b)
{
    if(a>b)
        return a;
    else
    return b;
}
bool cmp(const pair<int, int>& firs, const pair<int, int>& sec)
 {
  return firs.first < sec.first;
 }
int main()
{
double c,f,x;
int t,k;
i_n(t);
double r=2.0,t1=0;
double ans;
for(k=1;k<=t;k++)
{
    ans=0;
    r=2.0;
    cin>>c>>f>>x;
    double tm,tm1;
    while(1)
    {
        tm=x/r;
        tm1=(c/r)+(x/(r+f));
        if(tm<tm1)
        {
            ans+=tm;
            break;
        }
        ans+=c/r;
        r+=f;
    }
    printf("Case #%d: %0.7lf\n",k,ans);
}
 return 0;
}
