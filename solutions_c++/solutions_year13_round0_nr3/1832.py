#include <iostream>
#include <vector>
#include <sstream>
#include <cstdio>

using namespace std;

string int2str(long long i)
{
	string ans = "";
	while (i > 0)
	{
		ans = ans + (char)('0' + (i % 10));
		i /= 10;
	}
	return ans;
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<long long> ans;
	for (long long i = 1; i <= 10 * 1000 * 1000; ++i)
	{
		if (i % (100 * 1000) == 0)
		{
			fprintf(stderr, "%d\n", i);
		}
		string is = int2str(i);
		string is2(is);
		reverse(is2.begin(), is2.end());
		if (is != is2)
		{
			continue;
		}
		is = int2str(i * i);
		is2 = is;
		reverse(is2.begin(), is2.end());
		if (is == is2)
		{
			ans.push_back(i * i);
		}
	}
	int t;
	cin >> t;
	for (int T = 0; T < t; ++T)
	{
		long long a, b;
		cin >> a >> b;
		int ans2 = 0;
		for (int i = 0; i < (int)ans.size(); ++i)
		{
			if (ans[i] >= a && ans[i] <= b)
			{
				++ans2;
			}
		}
		cout << "Case #" << (T + 1) << ": " << ans2 << endl;
	}
	return 0;
}