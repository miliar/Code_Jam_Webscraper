#include <iostream>
using namespace std;

int D;
int P[1010];
int maxP;

void input() {
	scanf("%d", &D);
	maxP = -1;
	for(int i = 0; i < D; ++i) {
		scanf("%d", &P[i]);
		if(P[i] > maxP) maxP = P[i];
	}
}

int getMinu(int step) {
	int sum = 0;
	for(int i = 0; i < D; ++i) {
		sum += (P[i] - 1) / step;
	}
	return sum;
}

int mymin(int a, int b) {
	return a < b ? a : b;
}

void solve() {
	int ans = maxP;
	int step;
	step = 2;
	while(step < ans) {
		ans = mymin(ans, getMinu(step) + step);
		step ++;
	}
	printf("%d\n", ans);
}



int main() {
	//freopen("c:/aaa.txt", "r", stdin);
	freopen("c:/B-large.in", "r", stdin);
	freopen("c:/B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int ca = 0; ca < T; ++ca) {
		printf("Case #%d: ", ca + 1);
		input();
		solve();
	}
	return 0;
}