#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>

using namespace std;

int p[1024];
int p2[1024];
int D;
int ans = 10;
int tot = 0;

int cal(int bound) {
	int cnt = 0;
	for (int i = 0; i < D; i++)
		cnt += ceil(p[i] / (double)bound) - 1;
	return cnt;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	tot = 0;
	while (T--) {
		tot++;
		ans = 0;
		scanf("%d", &D);
		memset(p, 0, sizeof(p));
		for (int i = 0; i < D; i++)
			scanf("%d", &p[i]);

		for (int i = 0; i < D; i++)
			if (p[i] > ans) ans = p[i];

		for (int i = 1; i < 10; i++)
			if (cal(i) + i < ans) ans = cal(i) + i;

		printf("Case #%d: %d\n", tot, ans);
	}
	return 0;
}