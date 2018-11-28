#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <queue>
#include <deque>
#include <cctype>
#include <bitset>
#include <algorithm>
#include <iomanip>

using namespace std;

long double dp[1000][1000];
long double p[1000];

int main()
{
	int Cases;
	cin >> Cases;
	for (int Case = 1; Case <= Cases; Case++)
	{
		int N, K;
		cin >> N >> K;
		for (int i = 1; i <= N; i++)
			cin >> p[i];
		sort(p + 1, p + N + 1);
		double ans = 0.0;
		for (int i = 0; i <= K; i++)
		{
			memset(dp, 0, sizeof dp);
			dp[0][0] = 1;
			for (int j = 1; j <= K; j++)
			{
				double tmp;
				if (j <= i)
					tmp = p[j];
				else
					tmp = p[N - (j - i) + 1];
				dp[j][0] = (1 - tmp) * dp[j - 1][0];
				for (int k = 1; k <= j; k++)
					dp[j][k] = tmp * dp[j - 1][k - 1] + (1 - tmp) * dp[j - 1][k];
			}
			if (dp[K][K / 2] > ans)
				ans = dp[K][K / 2];
		}
		cout << "Case #" << Case << ": " << fixed << setprecision(12) << ans << endl;
	}
}