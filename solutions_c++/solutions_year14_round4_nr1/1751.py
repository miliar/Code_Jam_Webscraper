#include<cstdio>
#include<algorithm>
using namespace std;

int T, CN;
int n, x, s[10000];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (CN=1; CN<=T; CN++) {
		scanf("%d%d", &n, &x);
		for (int i=0; i<n; ++i)
			scanf("%d", s+i);
		printf("Case #%d: ", CN);
		sort(s, s+n);
		int start = 0, end = n-1, res = 0;
		while(start <= end) {
			while (s[start]+s[end] > x && start <= end) {
				--end;
				++res;
			}
			if (start <= end)
				++res;
			++start;
			--end;
		}
		printf("%d\n", res);
	}
	return 0;
}