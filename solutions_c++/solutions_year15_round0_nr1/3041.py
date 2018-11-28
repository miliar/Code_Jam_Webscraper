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
char st[10005];
int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;
  #ifdef O_judge
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
  #endif
    sn("%d",&t);
    while(t--)
    {
        sn("%d",&n);
        sn("%s",&st);s=0;a=0;
        for(i=0;i<n+1;i++)
        {
            if(a>=i)
            {
                a=st[i]-'0'+a;
            }
            else if(st[i]>'0')
            {
                s=s+(i-a);
                a=i+st[i]-'0';
            }
        }
        pf("Case #%d: %d\n",cs++,s);
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
