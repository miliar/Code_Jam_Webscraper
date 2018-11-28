#include <iostream>
#include <stdio.h>
using namespace std;

int main(void)
{
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-small-attempt2.out", "w", stdout);
	int T; cin >> T;
	for (int v = 1; v <= T; v++)
	{
		int ans = 0, count = 0, smax;
		cin >> smax;
		for (int i = 0; i <= smax; i++)
		{
			char ch; cin >> ch;
			if (ch != '0' && i > count)
			{
				ans += i - count;
				count = i;
			}
			count += ch - '0';
		}
		cout << "Case #" << v << ": " << ans << endl;
	}

	return 0;
}
