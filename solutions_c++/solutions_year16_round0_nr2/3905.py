#include <stdio.h>
#include <queue>
#include <iostream>
#include <string.h>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
int n;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int runs = 1;
	int T; for (scanf("%d", &T); T--; ) {
		string S;
		int res = 0;
		cin >> S; n = S.size();
		for (int i = 0; i < n; i++) {
			if (S[i] == '-') {
				int p = i;
				while (p < n && S[p] == '-') p++;
				if (i == 0) res++;
				else res += 2;
				i = p;
			}
		}
		printf("Case #%d: %d\n", runs++, res);
	}
	fcloseall();
	return 0;
}