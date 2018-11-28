/**************************************************************
    Problem:
    User: youmi
    Language: C++
    Result: Accepted
    Time:
    Memory:
****************************************************************/
//#pragma comment(linker, "/STACK:1024000000,1024000000")
//#include<bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <stack>
#include <set>
#include <sstream>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#define zeros(a) memset(a,0,sizeof(a))
#define ones(a) memset(a,-1,sizeof(a))
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scs(a) scanf("%s",a)
#define sclld(a) scanf("%I64d",&a)
#define pt(a) printf("%d\n",a)
#define ptlld(a) printf("%I64d\n",a)
#define rep0(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define rep_1(i,n) for(int i=n;i>=1;i--)
#define rep_0(i,n) for(int i=n-1;i>=0;i--)
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define lson (step<<1)
#define rson (lson+1)
#define esp 1e-6
#define oo 0x3fffffff
#define TEST cout<<"*************************"<<endl

using namespace std;
typedef long long ll;

int n,m;

const int maxn=200000+10;
int prime[maxn];
bool isprime[maxn];
int tot,pnt;
int a[50];
int b[50];
void get_prime()
{
    tot=0;
    memset(isprime,true,sizeof(isprime));
    isprime[0]=isprime[1]=false;
    for(int i=2;i<=maxn;i++)
    {
        if(isprime[i])
            prime[tot++]=i;
        for(int j=0;j<tot;j++)
        {
            if(1ll*prime[j]*i>maxn)
                break;
            isprime[prime[j]*i]=false;
        }
    }
}
void solve()
{
    ll ans=0;
    int cnt=0;
    for(int t=2;t<=10;t++)
    {
        for(int i=0;i<50;i++)
        {
            ans=0;
            ll bit=1%prime[i];
            ans=(ans+bit*a[n])%prime[i];
            for(int j=n-1;j>=1;j--)
            {
                bit=bit*t%prime[i];
                ans=(ans+bit*a[j])%prime[i];
            }
            if(ans==0)
            {
                b[t]=prime[i];
                cnt++;
                break;
            }
        }
    }
    if(cnt==9)
    {
        pnt++;
        for(int i=1;i<=n;i++)
            printf("%d",a[i]);
        for(int i=2;i<=10;i++)
            printf(" %d",b[i]);
        cout<<endl;
    }
}
void dfs(int temp)
{
    if(pnt>=m)
        return;
    if(temp>=n)
    {
        solve();
        return ;
    }
    a[temp]=0;
    dfs(temp+1);
    a[temp]=1;
    dfs(temp+1);
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    get_prime();
    int T_T;
    scanf("%d",&T_T);
    for(int kase=1;kase<=T_T;kase++)
    {
        sc2(n,m);
        printf("Case #%d:\n",kase);
        zeros(a);
        pnt=0;
        a[1]=a[n]=1;
        dfs(2);
    }
}
