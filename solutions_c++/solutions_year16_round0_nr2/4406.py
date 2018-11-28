#include <cstdio>
#include <cstring>
using namespace std;

char c[120], ln;

void runB() {
	freopen("b.out", "w", stdout);
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		scanf(" %s", c);
		ln = strlen(c);
		c[ln] = '*';
		int ans = 0;
		bool init = false;
		for (int i = 1; i <= ln; i++) {
			if (c[i] != c[i - 1]) {
				if (c[i - 1] == '-') {
					if (init) {
						ans += 2;
					}
					else {
						ans++;
					}
				}			   
				init = true;
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
}

int main() {
	runB();
}