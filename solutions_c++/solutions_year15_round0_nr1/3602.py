#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for (int i = 0; i < (n); i++)

int n;
char s[1111];

void test() {
	scanf("%d%s", &n, s);
	int cur = 0, res = 0;
	FOR(i,n+1) {
		res = max(res, i-cur);
		cur += s[i]-'0';
	}
	printf("%d\n", res);
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int ttt = 1; ttt <= tt; ttt++) {
		printf("Case #%d: ", ttt);
		test();
	}
	return 0;
}
