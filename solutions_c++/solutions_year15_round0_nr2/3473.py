#include <iostream>
#include <cstdio>

#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;
typedef long long ll;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int testcases = 1; testcases <= t; ++testcases)
	{
		ll res = 1e9;
		ll d;
		cin >> d;
		vector<ll> v(d);
		for (int i = 0; i < d; ++i)
			cin >> v[i];
		for (ll mx = 1000; mx > 0; mx--)
		{
			ll cur = 0;
			ll mm = 0;
			for (int i = 0; i < v.size(); ++i)
			{
				if (v[i]>mx)
				{
					cur += (v[i]-1) / mx;
				}
				mm = max(mm, v[i]);
			}
			res = min(res, cur + min(mm,mx));
		}
		cout << "Case #" << testcases << ": " << res<<endl;
	}
	return 0;
}