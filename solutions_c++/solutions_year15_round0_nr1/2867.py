#include<stdio.h>
char p[1010];
int main(){
	int TC, TT, n, i, S, Res;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d", &n);
		scanf("%s", p);
		S = 0, Res = 0;
		for (i = 0; i <= n; i++){
			if (Res < i-S){
				Res = i - S;
			}
			S += p[i] - '0';
		}
		printf("%d\n", Res);
	}
}