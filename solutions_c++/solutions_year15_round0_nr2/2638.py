#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main()
{
	ifstream fin("input1.in");
	ofstream fout("out1.txt");
	int tc;
	fin>>tc;
	for(int k = 1;k <= tc;k++)
	{
		ll d;
		fin>>d;
		ll a[1001];
		memset(a,0,sizeof(a));
		ll ans = 100000000000;
		for(int i = 0;i < d;i++)
		{
			int temp;
			fin>>temp;
			a[temp]++;
		}
		for(ll i = 1;i < 1001;i++)
		{
			ll sum = 0;
			for(ll j = i + 1;j < 1001;j++)
			{
				sum += (a[j]*(ceil((double)j/(double)i) - 1));
			}
			ans = min(ans,sum + i);
		}
		fout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
