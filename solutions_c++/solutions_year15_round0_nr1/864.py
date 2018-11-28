#include <iostream>
using namespace std;
int main()
{
	int T, smax, ans, now;
	char s[1100];
	cin >> T;
	for (int test = 1; test<=T; ++test)
	{
		cout << "Case #" << test << ": ";
		cin >> smax >> s;
		ans = now = 0;
		for (int i = 0; i <= smax; ++i)
		{
			int tmp = s[i] - '0';
			if (now < i)
			{
				ans += i - now;
				now = i;
			}
			now += tmp;
		}
		cout << ans << endl;
	}
}
