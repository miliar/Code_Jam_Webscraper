#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <list>
using namespace std;

int hibit(long long l)
{
	int bit = 0;
	while(l>0)
	{
		l/=2;
		bit++;
	}
	return bit;
}

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		long long n,p;
		cin >> n >>p;
		
		long long guarranted,possible;
		
		long long teams = 1;
		teams <<= n;
		long long rp = teams - p;
		int hibit_rp = hibit(rp);
		if(hibit_rp==0)
			guarranted = teams-1;
		else
		{
			guarranted = 0;
			long long delta = 1;
			for(int z=n-1;z>=hibit_rp;z--)
			{
				delta*=2;
				guarranted+=delta;
			}
		}
		if(p==1)
		{
			possible=0;
		}
		else
		{
			possible = 0;
			int hibit_p = hibit(p);
			long long delta = 1; delta <<=n;
			for(int z=1;z<hibit_p;z++)
			{
				delta/=2;
				possible+=delta;
			}
		}
		
		printf("Case #%d: %lld %lld\n", i, guarranted, possible);
	}
}
