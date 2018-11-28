#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int sum[1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, index = 1;
	cin >> T;
	while (T--)
	{
		memset(sum, 0, sizeof(sum));
		int smax; string line;
		cin >> smax >> line;
		sum[0] = line[0] - '0';
		int ans = 0;
		for (int i = 1; i <= smax; ++i)
		{
			ans = max(ans, i - sum[i - 1]);
			sum[i] = sum[i-1] + (line[i] - '0');
		}
		cout << "Case #" << index++ << ": " << ans << endl;
	}
	return 0;
}