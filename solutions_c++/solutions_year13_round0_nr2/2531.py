#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

int mas[100][100];
int maxr[100], maxc[100];
int t, n, m;


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("file.out", "w", stdout);

	cin >> t;
	for (int d = 1; d <= t; d++)
	{
		for (int i = 0; i < 100; i++)
		{
			maxr[i] = maxc[i] = 0;
		}

		cin >> n >> m;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &mas[i][j]);
				maxr[i] = max(mas[i][j], maxr[i]);
				maxc[j] = max(mas[i][j], maxc[j]);
			}
		}

		bool b = true;

		for (int i = 0; i < n && b; i++)
		{
			for (int j = 0; j < m && b; j++)
			{
				if (mas[i][j] < maxr[i] && mas[i][j] < maxc[j]) b = false;
			}
		}
		printf("Case #%d: ", d);
		if (!b) cout << "NO";
		else cout << "YES";
		cout << endl;
	}
	return 0;
}