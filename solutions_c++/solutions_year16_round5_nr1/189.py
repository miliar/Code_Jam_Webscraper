#include <bits/stdc++.h>

using namespace std;

int T, n;
char s[20010];
stack <char> S;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%s", s);
		while(!S.empty()) S.pop();
		n = strlen(s);
		int res = 0;
		for(int i = 0; i < n; i ++) {
			if(S.empty() || S.top() != s[i]) {
				S.push(s[i]);
			} else {
				res += 10;
				S.pop();
			}
		}
		res += S.size()/2 * 5;
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
