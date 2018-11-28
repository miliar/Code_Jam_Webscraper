#include <stdio.h>

int main()
{
	int tc, step = 0; scanf("%d", &tc);
	FILE* fin = fopen("A.txt", "w");
	while (step++ < tc){
		int n, ans = 0, sum = 0; scanf("%d", &n);
		
		for (int i = 0; i <= n; i++){
			int x; scanf("%1d", &x);
			if (sum < i){
				ans += i - sum;
				sum = i + x;
			}
			else sum += x;
		}
		fprintf(fin, "Case #%d: %d\n", step, ans);
	}
	return 0;
}