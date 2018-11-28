#include <cstdio>
#include <bitset>
using namespace std;

int main() {
	int t, m[5][5];
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		int x;
		scanf("%d", &x);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &m[i][j]);
		bitset<17> bs;
		for (int i = 1; i <= 4; ++i)
			bs[m[x][i]] = 1;
		scanf("%d", &x);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &m[i][j]);
		int ans = -1;
		for (int i = 1; i <= 4; ++i)
			if (bs[m[x][i]]) {
				if (ans == -1)
					ans = m[x][i];
				else
					ans = -2;
			}
		printf("Case #%d: ", tc);
		if (ans == -1) puts("Volunteer cheated!");
		else
		if (ans == -2) puts("Bad magician!");
		else
			printf("%d\n", ans);
	}
	return 0;
}
