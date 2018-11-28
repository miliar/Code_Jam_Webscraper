#include <algorithm>
#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

void solve(int t)
{
	string s;
	cin >> s;

	int res = 0;
	for (int i = s.length() - 1; i >= 0; --i)
	{
		if (s[i] == '+')
			continue;
		int j = 0;
		if (s[0] == '+')
		{
			for (j = 0; j < i && s[j] == '+'; ++j);
			reverse(s.begin(), s.begin() + j);
			for (int k = 0; k < j; ++k)
				s[k] = (s[k] == '+' ? '-' : '+');
			++res;
		}
		reverse(s.begin(), s.begin() + i + 1);
		for (int k = 0; k <= i; ++k)
			s[k] = (s[k] == '+' ? '-' : '+');
		++res;
	}

	cout << "Case #" << t + 1 << ": " << res << endl;
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		solve(i);
	}
	return 0;
}

