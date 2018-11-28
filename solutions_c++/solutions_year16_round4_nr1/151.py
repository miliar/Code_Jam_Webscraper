#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

string a[20][3];

bool check(string s, int x, int y, int z)
{
	for (int i = 0; i < (int)s.length(); i++)
	{
		if (s[i] == 'P')
			x--;
		if (s[i] == 'R')
			y--;
		if (s[i] == 'S')
			z--;
	}
	return x == 0 && y == 0 && z == 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	a[0][0] = "P";
	a[0][1] = "R";
	a[0][2] = "S";
	for (int k = 1; k < 14; k++)
	{
		string P = a[k - 1][0], R = a[k - 1][1], S = a[k - 1][2];
		a[k][0] = min(P + R, R + P);
		a[k][1] = min(P + S, S + P);
		a[k][2] = min(R + S, S + R);
	}
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		int n, x, y, z;
		cin >> n >> y >> x >> z;
		bool ok = false;
		for (int j = 0; !ok && j < 3; j++)
		{
			if (check(a[n][j], x, y, z))
			{
				cout << a[n][j] << endl;
				ok = true;
			}
		}
		if (!ok)
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}