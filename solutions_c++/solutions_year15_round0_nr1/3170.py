#include <cstdio>
#include <cstdlib>

const int N = 1005;
int test, tt;
int n;
char str[N];

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--) {
		scanf("%d", &n);
		scanf("%s", str);
		printf("Case #%d: ", ++tt);
		for (int i = 0; i <= n; i++) {
			int s = i, tag = 1;
			for (int j = 0; j <= n; j++) {
				if (s < j) {
					tag = 0;
					break;
				}
				
				s += str[j] - 48;
			}
			
			if (tag) {
				printf("%d\n", i);
				break;
			}
		}
	}
	
	return 0;
}

