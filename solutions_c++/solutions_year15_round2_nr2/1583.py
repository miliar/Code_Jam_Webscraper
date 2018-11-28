#include <bits/stdc++.h>
using namespace std;

int R, C, N;
int a[50][50];

int calculate(int x, int y)
{
	int result = 0;

	if (a[x - 1][y] == 1)
		result++;
	if (a[x][y - 1] == 1)
		result++;

	return result;
}

int main()
{
	freopen("B-input.txt", "r", stdin);
	freopen("B-output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> R >> C >> N;

		int result = 1000000000, m = R * C;

		for (int i = 1; i < (1 << m); i++)
		{
			int dem = 0;
			memset(a, 0, sizeof(a));

			for (int j = 0; j < m; j++)
				if ((i >> j) & 1)
					dem++;

			if (dem == N)
			{
				for (int j = 0; j < m; j++)
				{
					if (( i >> j) & 1)
					{
						int x = j + 1;
						int hang = (x / C) + (x % C != 0);
						int cot = x - (hang - 1) * C;
						a[hang][cot] = 1;
					}
				}

				int ans = 0;

				for (int u = 1; u <= R; u++)
					for (int v = 1; v <= C; v++)
						if (a[u][v] == 1)
							ans += calculate(u, v);

				result = min(result, ans);
			}
		}

		if (N == 0)
			result = 0;

		cout << "Case #" << t << ": " << result << "\n";
	}
	return 0;
}
