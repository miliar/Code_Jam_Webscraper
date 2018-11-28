#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
string s;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, sl, ans, cnt; 
	scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		cnt = ans = 0;
		scanf("%d", &sl);
		cin >> s;
		for (int i = 0; i <= sl; i++) {
			if (i > cnt) {
				ans += i - cnt;
				cnt = i + s[i] - '0';
			} else cnt += s[i] - '0';
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}