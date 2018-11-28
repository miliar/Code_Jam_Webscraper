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
#define Sd(x) scanf("%lf",&x)
#define S1(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define Pd(x) printf("%0.8lf\n",x)
#define P1(x) printf("%lld\n",x)
#define Ps(x) printf("%d ",x)
#define P1s(x) printf("%lld ",x)
#define Y printf("Bad magician!\n")
#define N printf("Volunteer cheated!\n")
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
	ll n,i,t,j,k;
	double x,f,c,ct,mt,mtc,pmt;
	for(S1(t),k=1;k<=t;k++)
	{
	    Sd(c);
	    Sd(f);
	    Sd(x);
	    mt=x/2;
	    mtc=c/2;
	    pmt=ct=1.0*mod;
	    for(i=1;pmt-mt>1e-10;i++)
        {
            pmt=mt;
            ct=mtc+x/(2+f*i);
            mtc=mtc+c/(2+f*i);
            if(ct<mt)
            {
                mt=ct;
            }
        }
        printf("Case #%lld: ",k);
        Pd(mt);
	}
	return 0;
}


