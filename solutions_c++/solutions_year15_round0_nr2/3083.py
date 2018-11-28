#include <iostream>
#include<stack>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<math.h>
#include<algorithm>
using namespace std;

#define gc getchar
#define MOD 1000000007
#define pc(x) putchar(x);
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define pis(n) printf("%d ",n)
#define pll(n) printf("%lld",n)
#define plls(n) printf("%lld ",n)
#define ps printf(" ")
#define pn printf("\n")
#define rep(i,n) for(i=0;i<n;i++)
#define fu(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define INV 333333336
#define ll long long
#define EPS 1e-9
#define infi 2000000000

inline ll sn()
{
    ll n=0;
    ll ch=gc();
    while( ch <48 )ch=gc();
    while( ch >47 )
    n = (n<<3)+(n<<1) + ch-'0', ch=gc();
        return n;
}


int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	
	int i,j,t,q,n,it,mini,g;
	int x[1005];
	t=sn();
	for(q=1;q<=t;q++)
	{
		n=sn();
		rep(i,n) x[i]=sn();
		mini=infi;
		fu(i,1,1000)
		{
			it=i;
			fu(j,0,n-1)
			{
				if(x[j]%i ==0)
					g=x[j]/i;
				else
					g=x[j]/i+1;
				it=it+g-1;
			}
			mini=min(it,mini);
		}
		printf("Case #%d: %d\n",q,mini);
	}

	return 0;
}














