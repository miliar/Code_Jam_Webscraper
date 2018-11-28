#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int T;
int n;
char s[1024];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%d %s", &n, s);
		int sum = 0, ans = 0;
		for (int i = 0; i <= n; i++) {
			int t = s[i] - 48;
			if (t > 0 && sum < i) {
				ans += i - sum;
				sum = i;
			}
			sum += t;
		}
		printf("%d\n", ans);
	}
	return 0;
}