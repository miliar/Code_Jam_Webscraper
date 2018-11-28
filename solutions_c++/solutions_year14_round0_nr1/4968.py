#include <cstdio>
#include <cstdlib>
using namespace std;
int T, w, x, b[20], a[20][20], cnt;
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &x);
		for (int i = 1; i <= 16; i++) b[i] = 0;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
			{
				scanf("%d", &a[i][j]);
				if (i == x) b[a[i][j]]++;
			}
		scanf("%d", &x);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
			{
				scanf("%d", &a[i][j]);
				if (i == x) b[a[i][j]]++;
			}
		cnt = 0;
		for (int i = 1; i <= 16; i++)
			if (b[i] == 2) cnt++, x = i;
		printf("Case #%d: ", ++w);
		if (cnt > 1) printf("Bad magician!\n");
		if (!cnt) printf("Volunteer cheated!\n");
		if (cnt == 1) printf("%d\n", x);
	}
	return 0;
}
