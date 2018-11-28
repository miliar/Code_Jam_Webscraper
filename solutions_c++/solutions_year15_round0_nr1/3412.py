#include <iostream>
#include <cstdio>

using namespace std;

const int N = 2000;

int n;
char st[N];

int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int cas = 1; cas <= test; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		scanf("%s", st);
		int ans = 0, s = 0;
		for (int i = 0; i <= n; i++) {
			if (st[i] > '0') {
				if (s < i) {
					ans += i-s;
					s = i;
				}
				s += st[i]-'0';
			}
		}
		cout << ans << endl;
	}
}
