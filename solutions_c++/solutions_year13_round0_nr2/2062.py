#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int f[100][100];
int n,m;
int r[100];
int c[100];

bool test()
{
	for (int i=0;i<n;++i)
	{
		for (int j=0;j<m;++j)
		{
			if (r[i] != f[i][j] && c[j] != f[i][j])
				return false;
		}
	}

	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;

	cin >> t;

	for (int i=0;i<t;++i)
	{
		memset(r, 0, sizeof(r));
		memset(c, 0, sizeof(c));

		cin >> n >> m;

		for (int x=0; x<n; ++x)
		{
			for (int y=0; y<m; ++y)
			{
				cin >> f[x][y];

				r[x] = max(r[x], f[x][y]);
				c[y] = max(c[y], f[x][y]);
			}
		}
		
		cout << "Case #" << i + 1 << ": ";

		bool ans = test();

		cout << (ans ? "YES" : "NO") << endl;
	}

	return 0;
}