#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int smax;
		string s;
		cin >> smax >> s;
		int ans = 0, cur = (int)s[0] - 48;

		for (int j = 1; j <= smax; j++)
		{
			if (cur < j)
			{
				ans += j - cur;
				cur = j;
			}
			cur += (int)s[j] - 48;
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
