#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXN = 100000;
const double eps = 1e-8;

int N, J, tot, Pri[MAXN], Num[MAXN], Fac[MAXN];
bool Flag[MAXN];

void GetPrime() {
	for (int i = 2; i <= MAXN; i ++) {
		if (!Flag[i]) Pri[++ tot] = i;
		for (int j = 1; j <= tot; j ++) {
			if (1ll * i * Pri[j] > MAXN) break;
			Flag[i * Pri[j]] = 1;
			if (i % Pri[j] == 0) break;
		}
	}
}

void Judge(int Side) {
	Fac[Side] = 0;
	for (int i = 1; i <= tot; i ++) {
		int S = 0;
		for (int j = N; j; j --) 
			S = (S * Side + Num[j]) % Pri[i];
		if (S == 0) {
			Fac[Side] = Pri[i];
			return;
		}
	}
}

bool Check() {
	for (int i = 2; i <= 10; i ++) {
		Judge(i);
		if (Fac[i] == 0) return 0;
	}
	for (int i = N; i; i --) printf("%d", Num[i]);
	for (int i = 2; i <= 10; i ++) printf(" %d", Fac[i]);
	printf("\n");
	return 1;
}

void Solve(int Side) {
	if (J == 0) return;
	if (Side == 0) {
		if (Check()) J --;
		return;
	}
	if (Side == 1 || Side == N) {
		Num[Side] = 1;
		Solve(Side - 1);
		if (Side == 0) return;
		return;
	}
	if (J == 0) return; Num[Side] = 0, Solve(Side - 1);
	if (J == 0) return; Num[Side] = 1, Solve(Side - 1);
	return;
}

int main() {
	//freopen("C.in", "r", stdin), freopen("C.out", "w", stdout);
	
	int Test;
	scanf("%d", &Test);
	scanf("%d%d", &N, &J);
	GetPrime();
	printf("Case #1:\n");
	Solve(N);
}