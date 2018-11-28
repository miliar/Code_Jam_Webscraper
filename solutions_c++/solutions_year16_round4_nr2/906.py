#include <cstdio>
int T, N, K;
double high;
double P[20], sum = 0;
bool B[20];
void f(int cnt, double P[], bool B[], int Yes, int No, double prob, double &cal){
	if (cnt == N){
		if (Yes == No)
			cal += prob;
	} else {
		if (!B[cnt]){
			f(cnt + 1, P, B, Yes, No, prob, cal);
		} else {
			f(cnt + 1, P, B, Yes + 1, No, prob * P[cnt], cal);
			f(cnt + 1, P, B, Yes, No + 1, prob * (1.0 - P[cnt]), cal);
		}
	}
}

void choice (int cnt, bool B[]){
	if (cnt == N){
		int sum = 0;
		for (int i = 0; i < N; i++)
			if (B[i])
				sum++;
		if (sum == K){
			double cal = 0.0;
			f(0, P, B, 0, 0, 1.0, cal);
			if (cal > high)
				high = cal;
		}
	} else {
		B[cnt] = true;
		choice (cnt + 1, B);
		B[cnt] = false;
		choice (cnt + 1, B);
	}
}
int main (){
	freopen ("B-small-attempt0.in", "r", stdin);
	freopen ("B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d", &N, &K);
		for (int j = 0; j < N; j++){
			scanf("%lf", &P[j]);
			B[j] = false;
		}
		high = 0.0;
		choice (0, B);
		printf("Case #%d: %llf\n", i, high);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
