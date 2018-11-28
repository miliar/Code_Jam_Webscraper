
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<set>
#include<iostream>
using namespace std;

#define S(x) scanf("%d",&x)
#define S1(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define P1(x) printf("%lld\n",x)
#define Ps(x) printf("%d ",x)
#define P1s(x) printf("%lld ",x)
#define Y printf("GOOD\n")
#define N printf("impossible\n")
#define mod 1000000007
#define ll long long

ll power(ll b, ll e) {
    ll p = 1;
    while (e > 0) {
        if(e&1) {
            p = (p*b)%mod;
        }
        e = e>>1;
        b = (b * b)%mod;
    }
    return p;
}
ll inp()
{
	ll n=0,s=1;
	char c;
	for(c=getchar_unlocked();c<48||c>58;c=getchar_unlocked())
	if(c=='-')s=-1;
	for(;c>47&&c<59;c=getchar_unlocked())
	n=n*10+c-48;
	return n*s;
}
int main()
{
	ll n,i,t,j,c,f,k=1,p,q,g;
	for(S1(t);k<=t;k++)
	{
	    scanf("%lld/%lld",&p,&q);
		g=__gcd(p,q);
		p/=g;
		q/=g;
        printf("Case #%lld: ",k);
        if((q&(q-1))!=0)
        {
            N;
            continue;
        }
		for(i=0;p<q;i++,q/=2);
        P1(i);
	}
	return 0;
}
