#include <bits/stdc++.h>
using namespace std;

int TC, N, L;

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d", &N, &L);
		bool fail = 0;
		string S;
		for (int i = 0; i < N; i++) {
			cin >> S;
			bool a_zero = 0;
			for (int j = 0; j < S.length(); j++) if (S[j] == '0') a_zero = 1;
			if (!a_zero) fail = 1;
		}
		cin >> S;
		if (fail) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		
		printf("Case #%d: ", tc);
		if (L == 1) printf("0 ?\n");
		else {
			printf("10?1");
			for (int i = 0; i < L - 2; i++) printf("01");
			printf(" ");
			for (int i = 0; i < L - 1; i++) printf("?");
			printf("\n");
		}
	}
}
