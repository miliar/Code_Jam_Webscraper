#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define pi 3.14159265359
int two[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 };
int p[11111] = { 0 };
int p2[11111] = { 0 };

int main()
{
	FILE **file = new FILE*;
	freopen_s(file, "input.txt", "r", stdin);
	freopen_s(file, "output.txt", "w", stdout);
	int t;
	cin >> t;
	int res, d, d2;
	int tekmin;
	int x, y, z;
	for (int i = 0; i < t; ++i)
	{
		cin >> d;
		d2 = d;
		for (int j = 0; j < d; ++j)
			cin >> p[j];
		sort(p, p + d);
		res = p[d - 1];
		for (int k = 0; k < 2048; ++k)
		{
			for (int j = 0; j < d; ++j)
				p2[j] = p[j];
			d2 = d;
			for (int tekmin = 0; tekmin < res;)
			{
				if (tekmin + p2[d2 - 1] < res)
					res = tekmin + p2[d2 - 1];
				if (k & two[tekmin])
				{
					x = p2[d2 - 1] / 2;
					y = p2[d2 - 1] - x;
					p2[d2 - 1] = x;
					p2[d2] = y;
					d2++;
					tekmin++;
				}
				else
				{
					x = p2[d2 - 1] / 3;
					y = (p2[d2 - 1] - x) / 2;
					z = p2[d2 - 1] - x - y;
					p2[d2 - 1] = x;
					p2[d2] = y;
					p2[d2 + 1] = z;
					d2 += 2;
					tekmin += 2;
				}
				sort(p2, p2 + d2);

			}
		}
		cout << "Case #" << i + 1 << ": " << res << "\n";
	}

	return 0;
}