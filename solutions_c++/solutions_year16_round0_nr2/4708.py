#include <bits/stdc++.h>

using namespace std;

int dp[110][2];

int main()
{
	int T;
	cin >> T;
	int cas = 0;
	while (T--)
	{
		cout << "Case #" << ++cas << ": ";
		string s;
		cin >> s;
		int size = s.size();
		if (s[0] == '+')
		{
			dp[0][0] = 0;
			dp[0][1] = 1;
		}
		else
		{
			dp[0][0] = 1;
			dp[0][1] = 0;
		}
		for (int i = 1; i < size; ++i)
		{
			if (s[i] == '+')
			{
				dp[i][0] = dp[i - 1][0];
				dp[i][1] = dp[i - 1][0] + 1;
			}
			else
			{
				dp[i][0] = dp[i - 1][1] + 1;
				dp[i][1] = dp[i - 1][1];
			}
		}
		cout << dp[size - 1][0] << endl;
	}


	return 0;
}