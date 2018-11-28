#include<stdio.h>
int w[1010];
int main(){
	int TC, TT, n, i, Res, S, j, t, M;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d", &n);
		for (i = 1; i <= n; i++){
			scanf("%d", &w[i]);
		}
		Res = 9999999;
		for (i = 1; i <= 1000; i++){
			S = 0, M = 0;
			for (j = 1; j <= n; j++){
				t = (w[j] - 1) / i;
				S += t;
				t = (w[j] - 1) / (t + 1) + 1;
				if (M<t)M = t;
			}
			if (Res > S + M)Res = S + M;
		}
		printf("%d\n", Res);
	}
}