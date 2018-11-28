#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for (int i = 0; i < (n); i++)

int p[1111];

void test() {
	int n;
	scanf("%d", &n);
	FOR(i,n) scanf("%d", &p[i]);
	sort(p,p+n);
	int res=1000;
	for (int d=1; d<=1000; d++) {
		int cur=d;
		FOR(i,n) cur += (p[i]+d-1)/d-1;
		res = min(res, cur);
	}
	printf("%d\n",res);
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
