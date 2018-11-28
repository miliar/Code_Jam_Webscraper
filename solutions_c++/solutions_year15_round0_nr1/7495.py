#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;
int main() {
	//freopen("large.in", "r", stdin);
	//freopen("data.out", "w", stdout);
	int T, tcase = 1;
	scanf("%d", &T);
	while (T--) {
		int S;
		string str;
		cin >> S >> str;
		int ans = 0, now = 0;
		for (int i = 0; i < str.length(); i++) {
			if (now >= i) {
				now += (str[i] - '0');
			}
			else {
				ans += (i - now);
				now += (i - now + (str[i] - '0'));
			}
		}
		printf("Case #%d: %d\n", tcase++, ans);
	}
	return 0;
}
