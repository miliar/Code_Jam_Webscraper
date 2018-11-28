#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int N;
int S[11], s[11], P[11], ss[11];

bool Chk[11];

int main(void)
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tt = 1; tt <= TC; tt++) {
		scanf("%d", &N);
		for (int i = 1; i <= N; i++) {
			scanf("%d", &S[i]);
			s[i] = S[i];
		}
		int f = 1;
		for (int i = 2; i <= N; i++) f *= i;
		int Cur = 0, Ans = 999999999;
		while (f--) {
			int Sw = 0;
			bool F = true;
			for (int i = 2; i <= N; i++) {
				if (S[i] < S[i - 1] && Sw == 0) {
					Sw = 1;
				}
				if (S[i] > S[i - 1] && Sw != 0) {
					F = false;
				}
				if (S[i] < S[i - 1] && Sw != 1) {
					F = false;
				}
			}
			if (F) {
				Cur = 0;
				for (int i = 1; i <= N; i++) ss[i] = s[i];
				for (int i = 1; i <= N; i++) {
					if (S[i] == ss[i]) continue;
					for (int j = N; j > 0; j--) {
						if (ss[j] == S[i]) {
							for (int k = j; k > i; k--) {
								swap(ss[k], ss[k - 1]);
								Cur++;
							}
							break;
						}
					}
				}
				Ans = min(Ans, Cur);
			}

//			for (int i = 1; i <= N; i++) printf("%d ", S[i]);
//			printf("\n");
			next_permutation(S + 1, S + N + 1);
		}
		printf("Case #%d: %d\n", tt, Ans);
	}

	return 0;
}
