#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

char s[111];
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas, cases;
	scanf("%d", &cas);
	for (cases = 1; cases <= cas; cases ++) {
		scanf("%s", s);
		int n = strlen(s);
		bool neg = false;
		int ans = 0;
		for (int i = 0; i < n; i++)
			if (s[i] == '-') {
				if (neg == false) {
					if (i == 0)	ans ++;
						else ans += 2;
				}
				neg = true;
			}
			else
				neg = false;
		printf("Case #%d: %d\n", cases, ans);
	}
}
