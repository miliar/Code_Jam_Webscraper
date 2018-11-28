#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	freopen("C:/Users/dd/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/dd/Downloads/A-large.out", "w", stdout);
	int cas;
	cin >> cas;
	for (int te = 1; te <= cas; te ++) {
		int n; cin >> n;
		string s; cin >> s;
		int ans = 0, cur = 0;
		for (int i = 0; i < s.length(); i++) {
			if (cur < i) {
				ans += (i - cur);
				cur = i;
			}
			cur += (s[i] - '0');
		}
		printf("Case #%d: %d\n", te, ans);
	} 
} 
