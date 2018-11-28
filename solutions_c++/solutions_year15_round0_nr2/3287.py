#include"bits/stdc++.h"
using namespace std;

const int D_MAX = 1000;
const int P_MAX = 1000;

int arr[D_MAX+1];

int main()
{
	cout.sync_with_stdio(false);
	cin.sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);

	int t;
	cin>>t;
	for(int cn = 1;cn<=t;++cn)
	{
		int d;
		cin>>d;
		for(int i = 0;i<d;++i)
		{
			cin>>arr[i];
		}
		int ans = numeric_limits<int>::max();
		for(int x = 1;x<=P_MAX;++x)
		{
			int pres = 0;
			for(int i = 0;i<d;++i)
			{
				pres+=(arr[i]-1)/x;
			}
			pres+=x;
			ans = min(ans,pres);
		}
		cout<<"Case #"<<cn<<": "<<ans<<"\n";
	}

	return 0;
}
