#include <stdio.h>
typedef long long ll;

int main() {
	int n;
	scanf("%d", &n);
	for (int ii = 0; ii < n; ++ii) {
		ll Num;
		scanf("%lld", &Num);
		int C[10] = { 0, };
		if (Num == 0) {
			printf("Case #%d: %s\n", ii + 1, "INSOMNIA");
			continue;
		}
		int k = 1;
		ll res;
		while (1){
			res = Num*k++;
			ll tmp = res;
			while (tmp) {
				if (!C[tmp % 10]) C[tmp % 10] = 1;
				tmp = tmp / 10;
			}
			int i = 0;
			for (i = 0; i < 10; ++i) if (!C[i]) break;
			if (i == 10) break;
		}
		printf("Case #%d: %lld\n", ii+1, res);
	}
	return 0;
}

