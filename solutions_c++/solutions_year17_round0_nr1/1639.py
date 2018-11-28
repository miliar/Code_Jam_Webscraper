#include <iostream>
using namespace std;

inline int solve(string& s, int k)
{
	int flips = 0;
	int l = s.length();

	for (int i = 0; i < l; ++i)
	{
		if (s[i] != '+')
		{
			if (i + k - 1 >= l)
				return -1;
			flips++;
			for (int j = 0; j < k; ++j)
				s[i + j] = (s[i + j] == '+' ? '-' : '+');
		}
	}

	return flips;
}

int main()
{
	int t, k;
	string s;

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s >> k;
		int flips = solve(s, k);
		if (flips != -1)
			cout << "Case #" << i << ": " << flips << endl;
		else
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}

