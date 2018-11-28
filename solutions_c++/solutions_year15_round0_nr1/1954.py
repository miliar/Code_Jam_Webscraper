#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int S;
		cin >> S;
		int cnt = 0;
		int ans = 0;
		for (int j = 0; j <= S; j++)
		{
			char c;
			cin >> c;
			if (c == '0')
			{
				continue;
			}
			int cur = c - '0';
			if (cnt >= j)
			{
				cnt += cur;
			}
			else
			{
				ans += j - cnt;
				cnt = j;
				cnt += cur;
			}
		}
		cout << "Case #" << i << ": " << ans << "\n";
	}







	return 0;
}