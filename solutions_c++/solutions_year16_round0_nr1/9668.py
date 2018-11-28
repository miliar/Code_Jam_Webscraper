#include <bits/stdc++.h>
using namespace std;
int mp[12];

void fill(long long m)
{
	while(m!=0)
	{
		mp[m%10]=1;
		m/=10;
	}
}

bool check()
{
	for(int l=0;l<=9;l++)
	{
		if(mp[l]==0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	// freopen("inp1.in","r",stdin);
	// freopen("out1.txt","w",stdout);
	int t;
	long long n;
	scanf("%d",&t);
	int tc=0;
	while(t--)
	{
		tc++;
		scanf("%lld",&n);
		for(int i=0;i<=9;i++)
		{
			mp[i]=0;
		}
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",tc);
		}
		else
		{
			long long ans = 1;
			long long final = 0;
			bool done = false;
			while(!done)
			{
				long long curr = n*ans;
				fill(curr);
				if(check())
				{
					done = true;
					final = curr;
				}
				ans++;
			}
			printf("Case #%d: %lld\n",tc,final);
		}
	}
}