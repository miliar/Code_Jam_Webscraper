#include <stdio.h>

int main()
{
	int tc, step = 0; scanf("%d", &tc);
	FILE* fout = fopen("B.txt", "w");
	while (step++ < tc){
		int n, p[1001] = { 0, }, max = 0; scanf("%d", &n);

		for (int i = 0; i < n; i++){
			int x; scanf("%d", &x);
			if (max < x) max = x;
			p[x]++;
		}

		int ans = max;
		for (int i = 1; i <= max; i++){
			int time = 0;

			for (int j = max; j > i; j--){
				if (!p[j]) continue;

				time += ((j - 1) / i) * p[j];
				if (time + i > ans) break;;
			}
			if (ans > time + i) ans = time + i;
		}

		fprintf(fout, "Case #%d: %d\n", step, ans);
	}
	return 0;
}