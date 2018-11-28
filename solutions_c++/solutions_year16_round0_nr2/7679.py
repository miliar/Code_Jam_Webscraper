#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;
char s[1010];
int main() {
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%s", s + 1);
		int ans = 0;
		for(int i = 1; s[i]; ++i) {
			if(i > 1 && s[i - 1] != s[i]) {
				ans++;
			}
			if(s[i] == '-' && s[i + 1] == '\0'){
				ans++;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}