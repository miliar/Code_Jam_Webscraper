#include <bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d",n)
#define piw(n) printf("%d ",n)
#define pin(n) printf("%d\n",n)
#define sorti(a) sort(a.begin(),a.end())
#define sortd(a) sort(a.begin(),a.end(),greater<__typeof(a[0])>()) 
#define LEN(s) s.length
#define SZ(s) s.size()

#define LL long long int
#define PII pair<int,int>
#define VI vector<int>
#define VPII vector< PII >
#define mod 1000000007
#define INF 2000000000

using namespace std;

int main()
{
	int t,x,r,c;
	si(t);
	for(int i=1;i<=t;i++)
	{
		si(x);
		si(r);
		si(c);
		printf("Case #%d: ",i);
		if(x==1)
		{
			printf("GABRIEL\n");
		}
		else if(x==2)
		{
			if((r*c)%2==0) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else if(x==3)
		{
			if((r*c)%3==0 && r!=1 && c!=1) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else if(x==4)
		{
			if((r*c)%4==0 && min(r,c)>=3) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else
		{

		}
	}
	return 0;
}