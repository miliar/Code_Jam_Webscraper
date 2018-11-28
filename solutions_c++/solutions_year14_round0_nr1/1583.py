#include <cstdio>

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i ++){
		printf("Case #%d: ", i+1);
		
		int a[5][5], b[5][5], r1, r2;
		scanf("%d", &r1);
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++)
				scanf("%d", &a[i][j]);
		scanf("%d", &r2);
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++)
				scanf("%d", &b[i][j]);
		int same = 0, ans = -1;
		for (int i = 0; i < 4; i ++)
			for (int j = 0; j < 4; j ++)
				if (a[r1-1][i] == b[r2-1][j])
					same ++, ans = a[r1-1][i];
		
		if (same == 1)
			printf("%d\n", ans);
		else if (same > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}
