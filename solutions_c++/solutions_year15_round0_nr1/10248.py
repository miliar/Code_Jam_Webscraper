#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, n;
char s[1005];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(int k = 1; k <= T; k++) {
		scanf("%d %s", &n, s);
		
		int cnt = 0, sum = s[0] - '0';
		for(int i = 1; i <= n; i++) {
			if(sum >= i) sum += (s[i] - '0');
			else {
				//printf("%d\n", i - sum);
				cnt += (i - sum);
				sum = i + (s[i] - '0');
			}
		}
		
		printf("Case #%d: %d\n", k, cnt);
	}
	return 0;
}
