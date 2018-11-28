#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n, tmp;
	cin >> t;
	for(int p = 1; p <= t; p++)
	{
		cin >> n;
		int MAX = 0, ans;
		vector<int> v;
		while(n--)
			cin >> tmp, v.push_back(tmp), MAX = max(MAX, tmp);
		ans = MAX;
		for(int i = 2; i <= ans; i++)
		{
			int sum = 0;
			for(int j = 0; j < v.size(); j++)
				if(v[j] > i)
					sum += (v[j]-1) / i;
			ans = min(ans, sum + i);
		}
		cout <<"Case #" << p << ": " << ans << endl;

	}

	return 0;
}