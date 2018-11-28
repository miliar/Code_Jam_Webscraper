#include<iostream>
#include<fstream>
#include<algorithm>

using namespace std;

int main() {
	freopen("counting_sheep.in", "r", stdin);
	freopen("counting_sheep.out", "w", stdout);
	int n, N, t, tm, i, j;
	bool dig[10];
	scanf("%d", &N);
	for (i = 0; i < N; ++i) {
		printf("Case #%d: ", i+1);
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		memset(dig, 0, sizeof(dig));
		t = 0;
		while (t >= 0) {
			t += n;
			tm = t;
			while (tm) {
				dig[tm % 10] = true;
				tm /= 10;
			}
			for (j = 0; j < 10; ++j)
				if (!dig[j])
					break;
			if (j == 10) {
				printf("%d\n", t);
				break;
			}
		}
		if (t < 0) {
			printf("INSOMNIA\n");
		}
	}
	return 0;
}