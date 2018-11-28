#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;

int main()
{
	int t;
	cin >> t;
	
	for (int test = 0; test < t; ++test)
	{
		double c, f, x;
		cin >> c >> f >> x;

		double cps = 2, curtime = 0;

		while (x / cps > c / cps + x / (cps + f))
		{
			curtime += c / cps;
			cps += f;
		}
		curtime += x / cps;

		cout.precision(20);
		cout << "Case #" << test + 1 << ": " << curtime << "\n";
	}

	return 0;
}
