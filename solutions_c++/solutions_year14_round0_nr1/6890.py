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
ll a[5][5],b[5][5];
int main()
{
	ll n,i,t,j,k,x,y,c;
	for(S1(t),k=1;k<=t;k++)
	{
	    c=0;
		S1(x);
		for(i=1;i<5;i++)
            for(j=1;j<5;j++)
            S1(a[i][j]);
		S1(y);
		for(i=1;i<5;i++)
            for(j=1;j<5;j++)
            S1(b[i][j]);
		for(i=1;i<5;i++)
            for(j=1;j<5;j++)
            {
                if(a[x][i]==b[y][j])
                {
                    c++;
                    n=a[x][i];
                }
            }
        printf("Case #%lld: ",k);
        if(c==1)
            P1(n);
        else if(c)Y;
        else N;

	}
	return 0;
}

