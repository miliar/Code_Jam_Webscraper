#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<bits/stdc++.h>
#include<malloc.h>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<deque>
#include<list>
#include<utility>
#include<stack>
#include<climits>
#include<cctype>
#define get getchar//_unlocked
#include<cassert>
#include<bitset>
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d",x)
#define pin(x) printf("%d",x)
#define sl(x) scanf("%lld",&x)
#define pl(x) printf("%lld",x)
#define pln(x) printf("%lld\n",x)
#define mp(a,b) make_pair(a,b)
#define pb push_back
#define ll long long
#define INF LONG_MAX
#define MOD 1000000007
#define clean(a) memset(a,0,sizeof(a));
#define fill(a,val) memset(a,val,sizeof(a));
#define printArray(a,n) for(ll macroi=0;macroi<n;macroi++)cout<<a[macroi]<<" "; cout<<endl;
using namespace std;
inline ll inp()
{
    ll n=0,s=1;
    char p=get();
    if(p=='-')
    s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
    p=get();
    if(p=='-')
    s=-1,p=get();
    while(p>='0'&&p<='9')
    {
    n = (n<< 3) + (n<< 1) + (p - '0');
    p=get();
    };
    return n*s;
}
long long power(ll a,ll b)
{
    long long r=1,x=a;
    while(b)
    {
        if(b&1)r=(r*x)%MOD;
        x=(x*x)%MOD;
        b>>=1;
    }
    return r%MOD;
}
long long mulmod(long long a,long long b,long long c)
{
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}

int main()
{
    ll i,j,k,t=1,r,w,x,y,z,n=0,m,test,l;
     //solve();
     //freopen("inp.txt","r",stdin);
     //freopen("out.txt","w",stdout);
     test=inp();
     for(t=1;t<=test;t++)
     {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double p=0,q=2;
        while(true)
        {
            if((c/q+ x/(q+f))<(x/q))
            {
                p+=c/q;
                q+=f;
            }
            else
            {
                p+=x/q;
                break;
            }

        }
        cout<<"Case #"<<t<<": ";
        printf("%.8lf\n",p);
     }
return 0;
}
