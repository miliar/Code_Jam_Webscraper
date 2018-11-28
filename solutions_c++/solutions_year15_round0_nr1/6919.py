#include <cstdio>
using namespace std;
int main(int argc, char *argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);
	int Case;
	scanf("%d", &Case);
	for (int x = 1; x <= Case; x++) {
		int shy;
		scanf("%d", &shy);
		int ans = 0, sum = 0;
		for (int i = 0; i <= shy; i++) {
			int now;
			scanf("%1d", &now);
			if (sum >= i) {
				sum += now;
			} else {
				ans += (i - sum);
				sum = now + i;
			}
		}
		printf("Case #%d: %d\n", x, ans);
	}
	return 0;
}
