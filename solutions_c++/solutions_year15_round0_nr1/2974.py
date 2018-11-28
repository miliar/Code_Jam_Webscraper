#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int now = 1; now <= test; now++) {
		int n;
		string s;
		cin >> n >> s;
		int ans = 0, total = 0;
		for (int i = 0; i <= n; i++) {
			if (total >= i) {
				total += (s[i] - '0');
			} else {
				ans++;
				total += 1 + (s[i] - '0');
			}
		}
		printf("Case #%d: %d\n", now, ans);
	} 
	return 0;
}