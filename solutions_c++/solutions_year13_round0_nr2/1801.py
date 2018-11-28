#include <cstdio>
using namespace std;

int mas[200][200] = {0};

bool isOk(int i0, int j0, int n, int m)
{
	int elem = mas[i0][j0];
	bool ok; 
	ok = true;
	for (int i = 1; i <= n; i++)
		if (mas[i][j0] > elem)
			ok = false;
	if (ok) return true;

	ok = true;
	for (int j = 1; j <= m; j++)
		if (mas[i0][j] > elem)
			ok = false;
	if (ok) return true;

	return false;
}

int calc(int n, int m)
{
	int res = 1;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
			if (!isOk(i, j, n, m))
				res = 0;
		}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int num;
	scanf("%d", &num);
	for (int k = 1; k <= num; k++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				scanf("%d", &mas[i][j]);
		int p = calc(n, m);
		printf("Case #%d: ", k);
		if (p == 0)
			printf("NO\n");
		else
			printf("YES\n");
	}

	return 0;
}