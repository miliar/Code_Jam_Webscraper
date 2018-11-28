#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;
int d, t, i, j, ans, x, r,c ,a;
void solve()
{
	cin >> x >> r >> c;
	if (r < c)
	{
		a = r;
		r = c;
		c = a;
	}
	if (x < 7 && (r*c) % x == 0 && r >= x&&c>=(x+1)/2)
	{
		if (x == 4 && c < 3) cout << "RICHARD" << endl;
		else cout << "GABRIEL" << endl;
	}
	else cout << "RICHARD" << endl;
}
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}