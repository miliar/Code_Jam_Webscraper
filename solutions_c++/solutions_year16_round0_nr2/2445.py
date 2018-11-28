#include <bits/stdc++.h>

using namespace std;

int T, cs = 0, n, Ret; char S[110];

int main (int argc, char const *argv[]) {
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T); while (T--) {
		scanf("%s", S + 1);
		n = strlen(S + 1);
		S[n + 1] = '+';
		Ret = 0;
		for (int i = 1; i <= n; i++) Ret += S[i] != S[i + 1];
		printf("Case #%d: %d\n", ++cs, Ret);
	}
	return 0;
}

