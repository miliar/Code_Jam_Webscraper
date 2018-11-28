/*@author KARTIK KESHRI */
#include<bits/stdc++.h>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<math.h>
#include<string.h>
using namespace std;
#define get getchar//_unlocked
#define mod 1000000007
#define s1(n) scanf("%d",&n)
#define p1(n) printf("%d\n",n)
#define s2(n) scanf("%lld",&n)
#define p2(n) printf("%lld\n",n)
#define s3(n) scanf("%lld",&n)
#define p3(n) printf("%lld\n",n)
#define st(s) scanf("%s",&s)
#define pst(s) printf("%s\n",s)
#define REP(i,n) for(i=0;i<(n);i++)
#define fill(a,b,c,x) for(i=b;i<=c;i++) a[i]=x;
#define sett(a,x) memset(a,x,sizeof(a))
#define sqr(x) x*x
#define MAX 10002
#define KARTIK  main
typedef unsigned long long int ull;
typedef long long int ll;
const long double PI = 3.1415926535897932384626433832795;

ll inp()
{
	ll n=0,s=1;
	char c;
	for(c=get();c<48||c>58;c=get())
	if(c=='-')s=-1;
	for(;c>47&&c<59;c=get())
	n=n*10+c-48;
	return n*s;
}

ll gcd(ll a,ll b)
{
     if(b==0)
     return a;
     else gcd(b,a%b);

}
// a^b%m


ll square(ll n) { return n*n; }

ll bigmod(ll b,ll p,ll m) {
if (p == 0)
return 1;
else if (p%2 == 0)
return square(bigmod(b,p/2,m)) % m; // square(x) = x * x
else
return ((b % m) * bigmod(b,p-1,m)) % m;
}


//exponentiation
long long mulmod(long long a,long long b,long long c){
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
char ch[2005];
ll a[1010];
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,i,j,k,ans=0,n,m;
    s2(t);
    for(k=1;k<=t;k++)
    {
        printf("Case #%lld: ",k);
        memset(a,0,sizeof(a));
        ans=0;
        ll men=0;
        s2(n);
        cin>>ch;
        for(i=0;i<(n+1);i++)
        {
            a[i]=ch[i]-48;
        }
        for(i=0;i<(n+1);i++)
        {
            if(a[i]==0)
                continue;
            if(i>men)
            {
                ans+=(i-men);
                men+=(i-men);
            }
            men+=a[i];
        }
        p2(ans);
    }
    return 0;
}
