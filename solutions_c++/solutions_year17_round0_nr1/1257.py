#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL;
typedef pair<int, int> II;

const int N = (int) 1e3 + 10;
int n, k;
char S[N];

int main() {
	int TC; scanf("%d", &TC);
	for (int testID = 1; testID <= TC; ++testID) {
		scanf("%s%d", S + 1, &k);
		n = strlen(S + 1);

		int ans = 0;
		for (int i = 1; i <= n - k + 1; ++i) {
			if (S[i] == '+') continue; ans++;
			for (int j = i; j <= i + k - 1; ++j) S[j] = (S[j] == '+') ? '-' : '+';
		}
		for (int i = 1; i <= n; ++i) if (S[i] == '-') ans = -1;

		printf("Case #%d: ", testID);
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
	return 0;
}