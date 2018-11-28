#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i <= (int)s.length() - k; ++i)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j < i + k; ++j)
					s[j] = (s[j] == '-') ? '+' : '-';
			}
		}
		bool possible = true;
		int i = max(0, (int)s.length() - k);
		for (; i < s.length(); ++i)
			if (s[i] == '-')
			{
				possible = false;
				break;
			}
		if (possible)
		{
			cout << "Case #" << t << ": " << ans << endl;
		}
		else
		{
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}