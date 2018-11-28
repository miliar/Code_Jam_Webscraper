#include <bits/stdc++.h>

using namespace std;

void optimizeIO()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
}

int main()
{
	optimizeIO();
	long long t, smax;
	string str;
	cin >> t;
	for (int T = 1; T <= t; T++)
	{
		cin >> smax >> str;
		long long a(0), s = str[0] - '0';
		for (int i = 1; str[i]; i++)
		{
			long long v = str[i] - '0';
			if (s < i)
			{
				a += i - s;
				s = i + v;
			}
			else
				s += v;
		}
		cout << "Case #" << T << ": " << a << '\n';
	}
	return 0;
}
