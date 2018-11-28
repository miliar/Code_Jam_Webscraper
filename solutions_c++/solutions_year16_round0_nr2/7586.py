#include <bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<sstream>

using namespace std;

#define open  freopen("B-large.in","r",stdin)
#define close  freopen ("B-large.out","w",stdout)
#define db double
#define ll long long
#define llu unsigned long long
#define loop(i,a,n) for(int i=a;i<=n;i++)
#define sf scanf
#define sf1(a) sf("%d",&a)
#define sf2(a,b) sf("%d %d",&a,&b)
#define sf3(a,b,c) sf("%d %d %d",&a,&b,&c)
#define sf4(a,b,c,d) sf("%d %d %d %d",&a,&b,&c,&d)
#define sfd(a) sf("%lf",&a);
#define sfd2(a,b) sf("%lf %lf",&a,&b)
#define sfl(a) sf("%lld",&a)
#define sfl2(a,b) sf("%lld %lld",&a,&b)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pf printf
#define bug pf("here is bug\n")
#define pft(tc) printf("Case: %d",tc++)
#define PI (2.0*acos(0.0))
//#define PI acos(-1.0)
#define mem(a,v) memset(a,v,sizeof a)
#define pb push_back
#define xx first
#define yy second
#define mp make_pair
#define inf 99999999
#define MX 1000006
#define mod (ll) 1000000007


template <class T> inline T bigmod(T p,T e,T M)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);
}   // M is prime}
template <class T> inline T bpow(T p,T e)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p);
        p = (p * p);
    }
    return (T)ret;
}


//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={0,1,0,-1};int dy[]={1,0,-1,0}; //4 Direction

struct zz
{
    int el1,el2;
    zz() {}
    zz(int a,int c)
    {
        el1=a,el2=c;
    }
    bool friend operator<(zz a,zz b)
    {
        return  a.el1> b.el1;// sort decreasingly but increasingly for priority_queue
    }
};


char a[105];
int vis[105];
int main()
{
//    open;
//    close;
    ll n;
    int t,tc=1;
    int cnt=0;
    sf1(t);
    while(t--)
    {
        mem(vis,0);
        sf("%s",a);
        int l=strlen(a);
        for(int i=0;i<l;i++)
        {

            if(a[i]=='-')
            {
                vis[i]=1;
            }
            //pf("%d %d\n",i,vis[i]);
        }
        int cnt=0;
        for(int i=l-1;i>=0;i--)
        {
            //pf("%d\n",vis[i]);
            if(vis[i]==1)
            {
                vis[i]=0;
                cnt++;
                for(int j=i-1;j>=0;j--)
                {
                    vis[j]=!vis[j];
                }
            }
        }
        pf("Case #%d:",tc++);
        pf(" %d\n",cnt);
    }

    return 0;
}

/*





*/


