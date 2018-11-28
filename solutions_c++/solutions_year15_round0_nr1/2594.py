#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; ++c)
	{
		int maxshy;
		cin >> maxshy;
		string aud;
		aud.reserve(maxshy+2);
		cin >> aud;
		int res = 0;
		int cur = 0;
		for (int i = 0; i <= maxshy; ++i)
		{
			if (cur < i)
			{
				res += i - cur;
				cur = i;
			}
			cur += aud[i] - '0';
		}
		cout << "Case #" << c << ": " << res << endl;
	}
	return 0;
}