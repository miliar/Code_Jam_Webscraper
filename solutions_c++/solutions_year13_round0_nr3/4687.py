#include<iostream>
#include<cstdio>
typedef long long LL;
using namespace std;
bool ok(LL n) {
	char str[100];
	int len = sprintf(str, "%lld", n);
	int i, j;
	for (i = 0, j = len - 1; i <= j; i++, j--) {
		if (str[i] != str[j]) {
			return false;
		}
	}
	return true;
}
void init() {
	LL i;
	for (i = 1; i <= 10000000; i++) {
		if (ok(i) && ok(i * i)) {
			printf("%lldLL,", i * i);
		}
	}
}
LL a[] = { 1LL, 4LL, 9LL, 121LL, 484LL, 10201LL, 12321LL, 14641LL, 40804LL,
		44944LL, 1002001LL, 1234321LL, 4008004LL, 100020001LL,
		102030201LL, 104060401LL, 121242121LL, 123454321LL,
		125686521LL, 400080004LL, 404090404LL, 10000200001LL,
		10221412201LL, 12102420121LL, 12345654321LL,
		40000800004LL, 1000002000001LL, 1002003002001LL,
		1004006004001LL, 1020304030201LL, 1022325232201LL,
		1024348434201LL, 1210024200121LL, 1212225222121LL,
		1214428244121LL, 1232346432321LL, 1234567654321LL,
		4000008000004LL, 4004009004004LL };
int main() {
	int T;
	LL x, y;
	int ans;
	int i;
	int ca = 1;
	freopen("C-large-1.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
//	init();
	cin >> T;
	while (T--) {
		ans = 0;
		cin >> x >> y;
		for (i = 0;; i++) {
			if (a[i] >= x && a[i] <= y) {
				ans++;
			}
			if (a[i] == 4004009004004LL) {
				break;
			}
		}
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}
