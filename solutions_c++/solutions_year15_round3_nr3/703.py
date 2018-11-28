#include <cstdio>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
	FILE *fin = fopen("C-small-attempt0.in", "r");
	FILE *fout = fopen("C-small-attempt0.out", "w");
	int TC;
	fscanf(fin, "%d", &TC);
	for (int TestCase = 1; TestCase <= TC; TestCase++) {
		int C, D, V;
		fscanf(fin, "%d %d %d", &C, &D, &V);
		// C : 갯수 제한 D : 동전 개수 V : V까지 만들어야 함
		int coins[10] = { 0, };
		int coin[50] = { 0, };
		int money[50] = { 1, };
		for (int i = 0; i < D; i++) {
			fscanf(fin, "%d", &coins[i]);
			coin[coins[i]] = 1;
			for (int j = V; j >= 0; j--) {
				if (j - coins[i] >= 0) {
					money[j] = money[j - coins[i]];
				}
			}
		}
		int requireCoins = 0;
		for (int i = 1; i <= V; i++) {
			if (money[i] == 0) {
				int optimalCoin = i;
				coin[optimalCoin] = 1;
				for (int j = V; j >= 0; j--) {
					if (j - optimalCoin >= 0 && money[j] == 0) {
						money[j] = money[j - optimalCoin];
					}
				}
				requireCoins++;
			}
		}
		fprintf(fout, "Case #%d: %d\n", TestCase, requireCoins);
	}
	return 0;
}