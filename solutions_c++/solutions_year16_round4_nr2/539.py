#include <cstring>
#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

const int MAXN = 205;

int N, K, Num;
double P[MAXN], D[MAXN], F[MAXN][MAXN];
double Ans;

void Solve() {
	memset(F, 0, sizeof F);
	F[0][0] = 1;
	for (int i = 1; i <= K; i ++) {
		for (int j = 1; j <= K; j ++) 
			F[i][j] = F[i - 1][j] * (1 - D[i]) + F[i - 1][j - 1] * D[i];
		F[i][0] = F[i - 1][0] * (1 - D[i]);
	}
	Ans = max(Ans, F[K][K / 2]);
}

void Work(int Ask) {
	printf("Case #%d: ", Ask);
	scanf("%d%d", &N, &K);
	Ans = 0;
	for (int i = 1; i <= N; i ++) cin >> P[i];
	sort(P + 1, P + 1 + N);
	for (int i = 0; i <= K; i ++) {
		Num = 0;
		for (int j = 1; j <= i; j ++) D[++ Num] = P[j];
		for (int j = N - (K - i) + 1; j <= N; j ++) D[++ Num] = P[j];
		Solve();
	}
	printf("%.10lf\n", Ans);
}

int main() {
	freopen("B.in", "r", stdin), freopen("B.out", "w", stdout);
	
	int Test;
	scanf("%d", &Test);
	for (int i = 1; i <= Test; i ++) Work(i);
}