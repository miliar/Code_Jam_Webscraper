#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char s[110], s1[110];
int main() {
	int T;
	int cas = 1;
	scanf("%d", &T);
	while (T--) {
		int ans = 0;
		scanf("%s", s);
		int l = strlen(s);
		int p = 0;
		s1[0] = s[0];
		for (int i = 1; i < l; i++) {
			if (s[i] != s[i - 1])
				s1[p++] = s[i];
		}
		if (s[0] == '-')
			ans++;
		for (int i = 0; i < p; i++) {
			if (s1[i] == '-')
				ans += 2;
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}
