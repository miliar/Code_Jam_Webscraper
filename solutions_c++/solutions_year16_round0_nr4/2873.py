#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 1001
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
vector<ll> str;
int main()
{
	int t,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		ll n,c,s,p;
		int i;
		str.clear();
		scanf("%lld%lld%lld",&n,&c,&s);
		printf("Case #%d: ",k);
		if(c==1)
		{
			for(i=1;i<=n;i++)
			  printf("%d ",i);
			printf("\n");
		}
		else
		{
			if(n==1)
			  printf("1\n");
			else if(n==2)
			{
			  printf("1 2\n");
			}
			else
			{
				printf("2 ");
				if(n%2==1)
				{
					for(i=n-1;i>=2;i-=2)
					  str.pb(i);
				}
				else
				{
					for(i=n-1;i>=3;i-=2)
					  str.pb(i);
				}
				for(i=0;i<str.size();i++)
				{
					p=str[i]*(n+1);
					printf("%lld ",p);
				}
				printf("\n");
			}

		}
	}
	return 0;
}
