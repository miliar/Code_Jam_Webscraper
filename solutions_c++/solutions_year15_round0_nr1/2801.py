#include <iostream>
#include <cstdio>
using namespace std;
const int Maxn = 1010;
int T, n;
char str[Maxn];
int main()
{
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d %s", &n, str);
		int ans = 0;
		int sum = 0;
		for (int i = 0; i <= n; ++i) {
			ans = max(ans, i - sum);
			sum += str[i] - '0';
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}