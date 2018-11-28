#include <stdio.h>
#include <algorithm>
using namespace std;

bool mat[4][4];
int perm[4];
int n;

bool verify(int t)
{
	if (t == n) return true;
	bool change[4] = {};
	bool nooo = false;
	for (int i = 0; i < n; i++)
	{
		if (mat[perm[t]][i])
		{
			nooo = true;
			for (int j = 0; j < n; j++)
			{
				change[j] = mat[perm[j]][i];
				mat[perm[j]][i] = false;
			}
			bool saved = verify(t + 1);
			for (int j = 0; j < n; j++)
			{
				mat[perm[j]][i] = change[j];
			}
			if (!saved) return false;
		}
	}
	return nooo;
}

int main()
{
	freopen(R"(C:\Users\Unused\Downloads\D-small-attempt2.in)", "r", stdin);
	freopen(R"(C:\Users\Unused\Downloads\D-small.out)", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d", &n);

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				char tmp;
				scanf(" %c", &tmp);
				mat[i][j] = tmp == '1';
			}
		}

		int ans = 99999;

		for (int i = 0; i < n; i++) perm[i] = i;

		for (int i = 0; i < (1 << (n * n)); i++)
		{
			bool wrong = false;
			for (int j = 0; j < n * n; j++)
			{
				if (i & (1 << j))
				{
					if (mat[j / n][j%n])
					{
						wrong = true;
						break;
					}
				}
			}
			if (wrong) continue;
			int biyong = 0;

			for (int j = 0; j < n * n; j++)
			{
				if (i & (1 << j))
				{
					biyong++;
					mat[j / n][j%n] = true;
				}
			}

			sort(perm, perm + n);
			do
			{
				if (!verify(0))
				{
					wrong = true;
					break;
				}
			} while (next_permutation(perm, perm + n));
			if (wrong == false)
			{
				ans = min(ans, biyong);
			}

			for (int j = 0; j < n * n; j++)
			{
				if (i & (1 << j))
				{
					mat[j / n][j%n] = false;
				}
			}
		}
		printf("%d\n", ans);
	}
}