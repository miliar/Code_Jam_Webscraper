#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		char S[101]; scanf("%s", S);
		char prev = S[0];
		int flip = (prev == '-') ? 1 : 0;
		for (int j = 1; S[j]; j++) {
			char curr = S[j];
			if (prev == '+' && curr == '-')
				flip += 2;
			prev = curr;
		}
		printf("Case #%d: %d\n", i, flip);
	}
}
