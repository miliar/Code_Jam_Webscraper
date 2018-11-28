#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
void init() {
	
}
char s[1010];
void solve() {
	int z = 0;
	scanf("%s", s);
	int len = strlen(s), i;
	if (s[0] == '-') z++;
	for (i = 0; i < len; i ++)
		if (s[i] == '+')
			break;
	while(i < len) {
		for (; i < len; i ++)
			if (s[i] == '-')
				break;
		if (i >= len) break;
		for (; i < len; i ++)
			if (s[i] == '+')
				break;
		z += 2;
	}
	printf("%d\n", z);
}
int main ()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++) {
		printf("Case #%d: ", i);
		init();
		solve();
	}
	return 0;
}

