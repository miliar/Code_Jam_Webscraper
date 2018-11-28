#include <cstdio>
#include <iostream>
using namespace std;

int T;
char S[1010];
char L;
int sum, need, thisNeed;
int main() {
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		sum = 0;
		need = 0;
		thisNeed = 0;
		scanf("%d", &L);
		cin >> S;
		for (int j = 0; j < L + 1; j++) {
			if (j) {
				if (j > sum && (S[j] - '0')) {
					thisNeed = j - sum;
					need += thisNeed;
				}
				else {
					thisNeed = 0;
				}
			}
			sum += S[j] - '0' + thisNeed;
		}
		printf("Case #%d: %d\n", i, need);
	}
	return 0;
}