#include <bits/stdc++.h>
 
 
 
#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define LL long long
#define F first
#define S second
#define pb push_back
#define mod (LL)(1e9+7)
#define LL long long
#define VVI vector< vector<int> >
#define MAXN 100000
#define MAXL 18
#define pii pair<int,int>
#define vpi vector< pair<int,int> >
#define vvpi vector< vector<pair<int,int>> >

using namespace std;
 


int main()
{
	int t;
	icin(t);
	int x=0;
	while(t--)
	{
		x++;
		vector<int> cnt(10,0);
		LL n,m;
		cin >> n;
		m=n;
		LL ans =0;
		if(n==0)
			ans = -1;
		else
		{
			int c=1;
			while(1)
			{
				LL x = m;
				while(x)
				{
					cnt[x%10]=1;
					x/=10;
				}
				int i;
				for(i=0;i<10;i++)
				{
					if(cnt[i]==0)
						break;
				}
				if(i==10)
					break;
				else
					m += n;
			}
		}
		if(ans==-1)
			printf("Case #%d: INSOMNIA\n",x);
		else
			printf("Case #%d: %lld\n",x,m);
	}

} 