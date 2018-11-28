#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;

int judge(int l[100][100], int n, int m)
{
	int b[100][100], h;
	for (int i = 0; i < n; i++)
	{
		h = l[i][0];
		for (int j = 0; j < m; j++)
			if (l[i][j] > h)
				h = l[i][j];
		for (int j = 0; j < m; j++)
			b[i][j] = h;
	}
	for (int j = 0; j < m; j++)
	{
		h = l[0][j];
		for (int i = 0; i < n; i++)
			if (l[i][j] > h)
				h = l[i][j];
		for (int i = 0; i < n; i++)
		{
			if (b[i][j] > h)
				b[i][j] = h;
		}
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (b[i][j] != l[i][j])
				return 0;
	return 1;
}

int main()
{
	//freopen("C:\\Users\\wayne\\Downloads\\input.txt", "r", stdin);
	//freopen("C:\\Users\\wayne\\Downloads\\output.txt", "w", stdout);
	freopen("C:\\Users\\wayne\\Downloads\\B-small-attempt1.in", "r", stdin);
	freopen("C:\\Users\\wayne\\Downloads\\Small-output.out", "w", stdout);
	//freopen("C:\\Users\\wayne\\Downloads\\A-large.in", "r", stdin);
	//freopen("C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t, n, m, l[100][100];

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n >> m;
		for (int j = 0; j < n; j++)
			for (int k = 0; k < m; k++)
				cin >> l[j][k];
		if (judge(l, n, m))
			cout << "Case #" << i << ": YES\n";
		else
			cout << "Case #" << i << ": NO\n";
	}
	return 0;
}