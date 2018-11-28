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
	int t,n,i,num,tot,ans;
	char c;
	si(t);
	for(int j=1;j<=t;j++)
	{
		si(n);
		for(ans=0,tot=0,i=0;i<n+1;i++)
		{
			cin>>c;
			num=c-'0';
			if(tot<i)
			{
				ans+=(i-tot);
				tot=i;
			}
			tot+=num;
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}