#include <cstdio>
#include <cstring>

void f (int pow, int R, int P, int S){
	if (pow == 2){
		if (R == 1 && P == 1){
			printf("PR");
		} else if (R == 1 && S == 1){
			printf("RS");
		} else if (P == 1 && S == 1){
			printf("PS");
		}
	} else {
		if (R % 2 == 0){
			if (R * 3 > pow){
				f(pow / 2, R / 2, P - R / 2 + 1, S - R / 2);
				f(pow / 2, R / 2, P - R / 2, S - R / 2 + 1);
			} else {
				f(pow / 2, R / 2, P - R / 2, S - R / 2 - 1);
				f(pow / 2, R / 2, P - R / 2 - 1, S - R / 2);
			}
		} else if (P % 2 == 0){
			if (P * 3 > pow){
				f(pow / 2, R - P / 2 + 1, P / 2, S - P / 2);
				f(pow / 2, R - P / 2, P / 2, S - P / 2 + 1);
			} else {
				f(pow / 2, R - P / 2, P / 2, S - P / 2 - 1);
				f(pow / 2, R - P / 2 - 1, P / 2, S - P / 2);
			}
		} else if (S % 2 == 0){
			if (S * 3 > pow){
				f(pow / 2, R - S / 2, P - S / 2 + 1, S / 2);
				f(pow / 2, R - S / 2 + 1, P - S / 2, S / 2);
			} else {
				f(pow / 2, R - S / 2 - 1, P - S / 2, S / 2);
				f(pow / 2, R - S / 2, P - S / 2 - 1, S / 2);
			}
		}
	}
}

int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	int T;
	int N, R, P, S;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d %d %d", &N, &R, &P, &S);
		int pow = 1;
		for (int j = 1; j <= N; j++)
			pow *= 2;
		int a = pow / 3;
		int b = pow / 3 + 1;
		if ((R == a || R == b) && (P == a || P == b) && (S == a || S == b) && R + P + S == pow){
			printf("Case #%d: ", i);
			f (pow, R, P, S);
			printf("\n");
		} else {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
