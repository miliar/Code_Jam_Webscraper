#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n;
	cin >> t;
	for(int p = 1; p <= t; p++)
	{
		vector<int> v;
		char c;
		cin >> n;
		getc(stdin);
		for(int i = 0; i < n + 1; i++)
		{
			c = getc(stdin);
			v.push_back(c-'0');
		}
		int sum = v[0], ans = 0;
		for(int i = 1; i < v.size(); i++)
		{
			if(v[i] && i > sum)
				ans += (i - sum), sum += (i - sum);
			sum += v[i];
		}
		cout <<"Case #" << p << ": " << ans << endl;
	}
	return 0;
}