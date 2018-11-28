#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int T, s, x, sum, ans;
	char c;
	cin >> T;
	for (int k = 1; k <= T; ++k)
	{
		sum = 0;
		ans = 0;
		cin >> s;
		for (int i = 0; i <= s; ++i)
		{
			cin >> c;
			x = c - '0';
			if (i > sum)
			{
				ans += i - sum;
				sum = i;
			}
			sum += x;
		}
		printf("Case #%d: %d\n", k, ans);
	}

	return 0;
}
