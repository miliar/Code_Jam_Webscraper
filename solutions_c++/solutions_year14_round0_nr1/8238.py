#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

#define EPS 1e-9

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("t2.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int a, b, p[4][4], q[4][4];
		cin >> a;
		for (int y = 0; y < 4; y++)
			for (int x = 0; x < 4; x++)
				cin >> p[x][y];
		cin >> b;
		for (int y = 0; y < 4; y++)
			for (int x = 0; x < 4; x++)
				cin >> q[x][y];
		--a;
		--b;
		int c = 0, d = -1;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
				if (p[x][a] == q[y][b])
					c++, d = p[x][a];
		printf("Case #%d: ", i+1);
		if (c == 0)
		{
			cout << "Volunteer cheated!";
		} else if (c == 1) {
			cout << d;
		} else {
			cout << "Bad magician!";
		}
		cout << endl;
	}
    return 0;
}
