#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define ll long long
#define mod 1000000007
#define pb(n) push_back(n)
#define maxn 1005
using namespace std;
int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		int x,r,c;
		si(x);si(r);si(c);
		int flag=0;
		if(r*c%x!=0)
			flag=0;
		else if(x==1)
		{
			flag=1;
		}
		else if(x==2)
		{
			if(r*c%2==0)
				flag=1;
		}
		else if(x==3)
		{
			if(r*c>3)
				flag=1;
		}
		else if(x==4)
			if(r*c>8)
				flag=1;
		if(flag)
		{
			printf("Case #%d: GABRIEL\n",i);
		}
		else
		{
			printf("Case #%d: RICHARD\n",i);
		}
	}
	return 0;
}