#include <cstdio>
using namespace std;

int num[1010], sum[1010];
char str[1010];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		printf("Case #%d: ", t);
		int n;
		scanf("%d", &n);
		scanf("%s", str);
		for (int i = 0; i <= n; i++) {
			num[i] = str[i] - '0';
		}
		int ans = 0;
		sum[0] = num[0];
		for (int i = 1; i <= n; i++) {
			sum[i] = sum[i - 1];
			if (sum[i] < i) {
				ans += i - sum[i];
				sum[i] = i;
			}
			sum[i] += num[i];
		}
		printf("%d\n", ans);
	}
	return 0;
}