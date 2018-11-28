#include <cstdio>
#include <cstring>

int a[100][50];
int h[100];
int mat[50][50];
int miss = -1;
int n;

bool check(int k, int t)
{
	for (int i = 0; i < k; ++i)
		if (i != miss && mat[k][i] != a[t][i])
			return false;
	return true;
}

bool search(int k)
{
	// fprintf(stderr, "%d\n", k);

	if (k == n)
		return true;
	if (k == miss)
	{
		return search(k + 1);
	}
	int t1 = -1, t2 = -1;
	for (int i = 0; i < 2 * n - 1; ++i)
		if (h[i] == k) {
			if (t1 == -1)
				t1 = i;
			else
				t2 = i;
		}

	if (check(k, t1))
	{
		for (int i = 0; i < n; ++i)
		{
			mat[k][i] = a[t1][i];
			mat[i][k] = a[t2][i];
		}
		bool t = search(k + 1);
		if (t)
			return true;
	}
	// else
	if (check(k, t2))
	{
		for (int i = 0; i < n; ++i)
		{
			mat[k][i] = a[t2][i];
			mat[i][k] = a[t1][i];
		}
		bool t = search(k + 1);
		if (t)
			return true;
	}

	return false;
}

void print() {
	int t1 = -1;
	for (int i = 0; i < 2 * n - 1; ++i)
		if (h[i] == miss)
		{
			t1 = i;
			break;
		}

	mat[miss][miss] = a[t1][miss];
	bool flag = true;
	for (int i = 0; i < n; ++i)
		if (mat[miss][i] != a[t1][i])
		{
			flag = false;
			break;
		}

	if (flag)
		for (int i = 0; i < n; ++i)
			printf("%d ", mat[i][miss]);
	else
		for (int i = 0; i < n; ++i)
			printf("%d ", mat[miss][i]);
}

int main () {
	freopen("B-small-attempt5.in", "r", stdin);

	// freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int ttt = 1; ttt <= T; ++ttt)
	{
		scanf("%d\n", &n);

		for (int i = 0; i < 2 * n - 1; ++i)
			for (int j = 0; j < n; ++j)
				scanf("%d", &a[i][j]);
		for (int i = 0; i < 2 * n; ++i)
			h[i] = -1;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				mat[i][j] = 0;

		for (int i = 0; i < n; ++i)
		{
			int min = 10000, pos = 0;
			for (int j = 0; j < 2 * n - 1; ++j)
				if (h[j] < 0 && a[j][i] < min)
				{
					min = a[j][i];
					pos = j;
				}
			h[pos] = i;
			bool flag = true;
			for (int j = 0; j < 2 * n - 1; ++j)
				if (h[j] < 0 && a[j][i] == min)
				{
					h[j] = i;
					flag = false;
					break;
				}
			if (flag)
				miss = i;
		}
		// fprintf(stderr, "%d\n", miss);

		search(0);
		printf("Case #%d: ", ttt);
		print();
		printf("\n");

		// for (int i = 0; i < n; ++i)
		// {
		// 	for (int j = 0; j < n; ++j)
		// 		printf("%d ", mat[i][j]);
		// 	printf("\n");
		// }
		// 	printf("\n");

	}

	return 0;
}
