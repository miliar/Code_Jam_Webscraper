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
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t=sn();
	int q;
	for(q=1;q<=t;q++)
	{
		int i,j,n,ans1,ans2,maxi;
		n=sn();
		int x[n];
		rep(i,n) x[i]=sn();
		ans1=0;
		ans2=0;
		fu(i,1,n-1)
		{
			if(x[i]<x[i-1]) 
				//{pis(i);pis(x[i-1]);pin(x[i]);
				ans1=ans1+x[i-1]-x[i];//pin(ans1);}
		}
		//pin(ans1);
		if(x[n-2]-x[n-1] > 0)
			maxi=x[n-2]-x[n-1];
		else 
			maxi=0;
			
		maxi=0;
		fu(i,0,n-2)
			maxi=max(maxi,x[i]-x[i+1]);	
			
		fu(i,0,n-2)
		{
			ans2=ans2+min(x[i],maxi);
		}
		printf("Case #%d: %d %d\n",q,ans1,ans2);
		

	}

	return 0;
}














