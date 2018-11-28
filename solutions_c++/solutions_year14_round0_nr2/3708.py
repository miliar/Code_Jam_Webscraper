#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <string>
using namespace std;
int t;
const long double EPS = 1e-9;

void solve()
{
	long double c, f, x, curs = 2.0, curt = 0, mint = 1e9;
	cin >> c >> f >> x;
	while (curt < x && mint > curt)
	{
		mint = min (mint, curt + x / curs);
		curt += c / curs;
		curs += f;
	}

	printf("%.7lf\n", (double)mint);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}