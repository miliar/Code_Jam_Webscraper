#include <bits/stdc++.h>
using namespace std;
int main()
{
	int tc, t = 1;
	cin >> tc;
	int a[10000];
	while(tc--)
	{
		int d, ans = 0;
		cin >> d;
		for(int i=0; i<d; ++i)
		{
			cin >> a[i];
			if(a[i] > ans)
			{
				ans = a[i];
			}
		}
		int tmpmax = ans;
		for(int i = 1; i<=tmpmax; ++i)
		{
			int cuts = 0;
			for(int j = 0; j<d; ++j)
			{
				if(a[j] % i == 0)
				{
					cuts += (a[j]/i)-1;
				}
				else
				{
					cuts += (a[j]/i);
				}
			}
			if(cuts + i < ans) ans = cuts + i;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
        t++;
	}
	return 0;
}