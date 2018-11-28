#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i, j, k, t, n, m, x, y, r, c;
	cin >> t;
	for (y = 1; y <= t; ++y)
	{
		cin >> x >> r >> c;
		int flag = 2;
		if (x >= 7)
			flag = 0;
		else if ((r%x == 0 || c%x == 0) && (r>(x - 2) && c > (x - 2)))
		{
			flag = 1;
		}
		else
			flag = 0;
		cout << "Case #" << y << ": ";
		if (flag == 0)
			cout << "RICHARD\n";
		else
			cout << "GABRIEL\n";
	}
}