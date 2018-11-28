#define Fractiles_L

#ifdef Fractiles_L
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	//freopen("in.txt","rt",stdin);
	freopen("D-small-attempt1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);

		if (C!=1) {
			vector <unsigned long long> position;

			int min = (K+K%2)/2;
			if (S < min) {
				printf("Case #%d: IMPOSSIBLE\n", i);
				continue;
			}
			else {
				printf("Case #%d: %", i);
				for (int j = 1; j <= min; j++) {
					if ((unsigned long long)2 * (unsigned long long)j>K)
						printf("%llu ", (unsigned long long)K);
					else {
						unsigned long long val = ((unsigned long long)2 * (j - 1)*(unsigned long long)powl((unsigned long long)K, (unsigned long long)C - 1)) + (unsigned long long)2 * (unsigned long long)j;
						printf("%llu ", val);
					}
				}
				for (int j = min + 1; j <= S; j++) {
					unsigned long long val = j - min;
					if (val!=2)
						printf("%llu ", val);
				}
				printf("\n");
			}
			/*
			for (int j = 1; j <= S; j++) {
				position.push_back(j);
			}

			if (position.size() == 0)
				printf("Case #%d: IMPOSSIBLE\n", i);
			else {
				printf("Case #%d: %", i);
				for (int j = 1; j <= S; j++) {
					printf("%llu ", position[j - 1]);
				}
				printf("\n");
			}
			*/
		}
		else {
			if (K != S) {
				printf("Case #%d: IMPOSSIBLE\n", i);
			}
			else {
				printf("Case #%d: %", i);
				for (int j = 1; j <= S; j++) {
					printf("%d ", j);
				}
				printf("\n");
			}
		}
	}

	return 0;
}

#endif