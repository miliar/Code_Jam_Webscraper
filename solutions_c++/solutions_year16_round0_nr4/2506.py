#include <bits/stdc++.h>
using namespace std;
int K, C, S;

void solveSmall() {
	for(int i = 1; i <= K; i++) {
		printf(" %d", i);
	}
	printf("\n");
}
void solveBig() {
	return;
}
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.ou", "w", stdout);
	int T, cases = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", ++cases);
		solveSmall();
		//solveBig();
	}
	return 0;
}
