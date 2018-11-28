#include <bits/stdc++.h>

using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int target = (1LL << 10) - 1;

void openFile() {
	freopen("in.inp", "r", stdin);
	freopen("ou.out", "w", stdout);
}

int onBit(int N, int &status) {
	do {
		status |= (1LL << (N % 10));
		N /= 10;
	} while (N > 0);
}

int solve(int N) {
	int status = 0, i = 1;
	for (i = 1; status != target; ++i) onBit(N * i, status);
	return N * (i - 1);
}

int main(int argc, char **argv) {
	openFile();
	int N, T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		scanf("%d", &N);
		printf("Case #%d: ", i + 1);
		if (N == 0) printf("INSOMNIA");
		else printf("%d", solve(N));
		printf("\n");
	}
	return 0;
}
