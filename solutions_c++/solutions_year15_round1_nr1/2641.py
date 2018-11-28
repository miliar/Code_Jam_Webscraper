#include <cstdio>

#define INF 100000000

using namespace std;

int N, m[10003];

int max(int a, int b) {
	return (a > b ? a : b);
}

int min(int a, int b) {
	return (a < b ? a : b);
}

int main(int argc, char const *argv[])
{
	freopen("iLA.in", "r", stdin);
	freopen("oLA.txt", "w", stdout);
	int tc, T, i, y, z, r, j, temp;
	scanf("%d", &T);
	for(tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		scanf("%d", &N);
		r = 0;
		for(i = 0; i < N; i++) {
			scanf("%d", &m[i]);
			r = max(r, m[i]);
		}
		y = 0;
		for(i = 1; i < N; i++) {
			if(m[i] < m[i - 1])
				y = y + m[i - 1] - m[i];
		}
		z = INF;
		for(i = 0; i <= r; i++) {
			temp = 0;
			for(j = 0; j < N - 1; j++) {
				int left = m[j] - i;
				if(left < 0) left = 0;
				if(left > m[j + 1]) {
					temp = INF;
					break;
				}
				temp = temp + m[j] - left;
			}
			z = min(z, temp);
		}
		if(z == INF) z = 0;
		printf("%d %d\n", y, z);
	}
	return 0;
}