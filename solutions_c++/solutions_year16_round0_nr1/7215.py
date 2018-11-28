#include <cstdio>
#include <cstring>

int main()
{
	int T, N;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", cases);
			continue;
		}
		bool v[10];
		memset(v, 0, sizeof(v));
		int tot = 0;
		int cnt = N;
		while (1) {
			int tmp = cnt;
			while (tmp) {
				if (!v[tmp % 10])
					v[tmp % 10] = 1, ++tot;
				tmp /= 10;
			}
			if (tot == 10)
				break;
			cnt += N;
		}
		printf("Case #%d: %d\n", cases, cnt);
	}
}
