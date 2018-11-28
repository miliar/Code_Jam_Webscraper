#include <bits/stdc++.h>
using namespace std;
const int maxn = 105;
char str[maxn];

bool check(char *s, int len) {
	for(int i = 0; i < len; i++) if(str[i] == '-') return false;
	return true;
}
int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.ou", "w", stdout);
	int T, cases = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%s", str);
		int len = strlen(str);
		int cnt = 0;
		while(!check(str, len)) {
			bool flag = 0;
			for(int i = 0; i < len; i++) {
				if(str[i] == '-') {
					str[i] = '+';
					flag = 1;
				} else {
					break;
				}
			}
			cnt += flag;
			flag = 0;
			for(int i = len - 1; i >= 0; i--) {
				if(str[i] == '-') {
					reverse(str, str + i + 1);
					flag = 1;
					break;
				}
			}
			cnt += flag;
		}
		printf("Case #%d: %d\n", ++cases, cnt);
	}
	return 0;
}
