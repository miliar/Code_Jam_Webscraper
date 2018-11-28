#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <unordered_map>

using namespace std;

int possible[17][3]; // P R S
long long bestScore[17][3];
int bestShift[17][3];

void populate() {
	possible[1][0] = 1;
	possible[1][1] = 1;
	possible[1][2] = 0;

	bestScore[1][0] = 1;
	bestScore[1][1] = 2;
	bestScore[1][2] = 3;

	for (int i = 2; i <= 16; ++i) {
		for (int j = 0; j < 3; ++j) {
			int o = (j + 2) % 3;
			possible[i][j] = possible[i-1][j] + possible[i-1][o];
			int best = (bestScore[i-1][j] < bestScore[i-1][o]) ? j : o;
			int worst = j + o - best;
			bestShift[i][j] = best;
			bestScore[i][j] = bestScore[i-1][best] * (1LL << (i*2)) + bestScore[i-1][worst];
		}
	}
}

void printBest(int level, int shift) {
	//printf("\n%d %d\n", level, shift);
	if (level == 1) {
		if (shift == 0) printf("PR");
		if (shift == 1) printf("PS");
		if (shift == 2) printf("RS");
		return;
	}


	int ot = (shift + 2) % 3;
	printBest(level - 1, bestShift[level][shift]);
	printBest(level - 1, ot + shift - bestShift[level][shift]);
}

void test(int number)
{
	int N, R, P, S;
	cin >> N >> R >> P >> S;

	//printf("%d %d %d\n", possible[N][0], possible[N][1], possible[N][2]);
	printf("Case #%d: ", number + 1);
	if (possible[N][0] == P && possible[N][1] == R && possible[N][2] == S)
		printBest(N, 0);
	else if (possible[N][0] == S && possible[N][1] == P && possible[N][2] == R)
		printBest(N, 1);
	else if (possible[N][0] == R && possible[N][1] == S && possible[N][2] == P)
		printBest(N, 2);
	else
		printf("IMPOSSIBLE");

	printf("\n");
	
}

int main(int argc, char *argv[])
{
	populate();
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
		test(t);
	return 0;
}