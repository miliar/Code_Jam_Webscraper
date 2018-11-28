#include <bits/stdc++.h>
using namespace std;
int n, T;
char s[1111];
int cnt[1111];
int main(){	
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &T);
	for (int test = 1; test <= T; test++){
		scanf("%d %s", &n, &s);
		for (int i = 0; i <= n; i++){
			int t = s[i] - '0';
			cnt[i] = t;
		}

		int standing = 0;
		int friends = 0;
		for (int i = 0; i <= n; i++){
			if (standing < i) {
				friends += i - standing;
				standing = i;
			}
			standing += cnt[i];
		}
		printf("Case #%d: %d\n", test, friends);
	}
	return 0;
}