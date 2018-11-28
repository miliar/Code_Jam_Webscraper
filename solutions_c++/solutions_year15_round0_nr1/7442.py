#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t, n, curSum, ans; char c;
	cin >> t;
	for (int test = 1; test <= t; test++)
	{
		cin >> n;
		curSum = ans = 0;
		for (int i = 0; i <= n; i++)
		{
			cin >> c;
			if (curSum < i && c != '0') {
				ans += i - curSum;
				curSum += i - curSum + (c - '0');
			} 
			else if (c != '0') {
				curSum += (c - '0');
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}