//BISMILLAHIR RAHMANIR RAHIM
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<queue>
#include<set>
#include <iostream>
#include<stack>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#define N 1000000
#define sn scanf
#define pf printf
#define pb push_back

typedef long long int ll;
using namespace std;
struct T{
int a;
};
ll bigmod(ll a,ll b,ll mod)
{
    if(b==0)return 1;
    if(b%2==0)
    {
        ll hh=bigmod(a,b/2,mod);
        return (hh*hh)%mod;
    }
    else
    {
       return (a*bigmod(a,b-1,mod))%mod;
    }
}
int ar[10005];
int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;
  #ifdef O_judge
      freopen("B-large.in","r",stdin);
      freopen("out.txt","w",stdout);
  #endif
    sn("%d",&t);
    while(t--)
    {
        sn("%d",&n);s=0;
        for(i=0;i<n;i++)
        {
            sn("%d",&u);
            ar[i]=u;
            s=max(s,u);
        }

        g=s;
        for(i=1;i<=g;i++)
        {
            a=0;h=0;v=0;
            for(j=0;j<n;j++)
            {
                if(ar[j]<=i)continue;
                b=(ar[j]/i);
                if(ar[j]%i!=0)
                {
                    h=max(h,ar[j]%i);v++;
                }
                b=max(0,b-1);
                a=a+b;
            }
            s=min(s,a+i+min(h,v));
        }
        pf("Case #%d: %d\n",cs++,s);
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
