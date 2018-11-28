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
#define mp make_pair

const double PI=2.0*acos(0);

typedef long long int ll;
using namespace std;
struct T{
int a;
};
struct vec{
double x,y;
 vec(double xx=0,double yy=0)
 {
     x=xx;y=yy;
 }
};
vec make_vac(vec p,vec q)
{
    return vec(q.x-p.x,q.y-p.y);
}
double dotproduct(vec p,vec q)
{
    return p.x*q.x+p.y*q.y;
}
double crossproduct(vec p,vec q)
{
    return p.x*q.y-q.x*p.y;
}
double vec_value(vec p)
{
    return sqrt(p.x*p.x + p.y*p.y);
}
vec unit_vec(vec p)
{
    double va=vec_value(p);
    return vec(p.x/va,p.y/va);
}
double dis(double px,double py,double qx,double qy)
{
    px=fabs(px-qx);
    py=fabs(py-qy);
    return sqrt(px*px+py*py);
}
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
int dp[1<<11];
int rec(int msk,int k,int n)
{
    if(msk==(1<<n)-1)
        return 0;
    int &ret=dp[msk];
    if(ret!=-1)
        return ret;
    ret=100000000;
    int xr=(1<<k)-1;
    for(int i=0;i<=n-k;i++)
    {
        ret=min(ret,1+rec(msk^xr,k,n));
        xr=xr<<1;
    }
    return ret;
}
char st[3333];
int ar[3333];
int main()
{
    int i,j,k,l,t,cs=1,r=1,s,m,n,a,b,c,d,e,f,g,h,u,v;

   //freopen("A.in","r",stdin);
   // freopen("out.txt","w",stdout);
    sn("%d",&t);
    while(t--)
    {
        sn("%s %d",&st,&k);
        l=strlen(st);
        m=0;
        for(i=0;i<l;i++)
        {
            if(st[i]=='+')
             ar[i]=1;
            else
              ar[i]=0;
        }
        int ans=0;
        for(i=0;i<=l-k;i++)
        {
            if(ar[i]==0)
            {
                ans++;
                for(j=0;j<k;j++)
                    ar[i+j]=1-ar[i+j];
            }
        }
        for(i=0;i<l;i++)
        {
            if(ar[i]==0)
                ans=-111;
        }
        if(ans<0)
            pf("Case #%d: IMPOSSIBLE\n",cs++);
        else
            pf("Case #%d: %d\n",cs++,ans);
    }
    return 0;

}

/*
#include <bits/stdc++.h>
  #define _ ios_base::sync_with_stdio(0);cin.tie(0);
*/
