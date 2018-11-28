#include <bits/stdc++.h>

using namespace std;

int n, t, cnt[10];

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin >> n;
		memset(cnt, 0, sizeof cnt);
		long long ans = -1;
		for (int i = 1; i <= 100000; i++)
		{
			long long v = (long long)i * (long long)n;
			stringstream ss;
			string s;
			int sum = 0;
			ss << v;
			ss >> s;
			for (int j = 0; j < s.length(); j++)
				cnt[s[j] - '0'] = 1;
			for (int j = 0; j < 10; j++)
				sum += cnt[j];
			if (sum == 10)
			{
				ans = v;
				break;
			}
		}
		if (ans != -1)
			cout << "Case #" << tt << ": " << ans << endl;
		else
			cout << "Case #" << tt << ": " << "INSOMNIA" << endl;
	}
	return 0;
}