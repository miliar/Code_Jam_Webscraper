#include<bits/stdc++.h>
#define rep(i, a, b) for(int i = a; i <= b; i++)
using namespace std;

char s[10005];
int n;
bool check() {
	rep(i, 1, n)
		if(s[i] == '-')
			return false;
	return true;
}
int main () {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int tc;
	cin >> tc;
	rep(tt, 1, tc) {
		scanf("%s", s + 1);
		n = strlen(s + 1);
		int k;
		cin >> k;
		int ans = 0;
		rep(i, 1, n-k+1) {
			if(s[i] == '-') {
				ans ++;
				rep(j, i, i+k-1) {
					if(s[j] == '+') {
						s[j] = '-';
					}
					else {
						s[j] = '+';
					}
				}
			}
		}
		if(check()) {
			printf("Case #%d: %d\n", tt, ans);
		}
		else
			printf("Case #%d: IMPOSSIBLE\n", tt);
	}
	return 0;
}