#include <stdio.h>
#include <string.h>
const int maxLen = 2000;
int main()
{	int T;
	int ans, Smax;
	char list[maxLen +1];
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		ans = 0;
		scanf("%d %s", &Smax, list);

		int accu = 0;
		for (int i = 0; i <= Smax; ++i) {
			if (i > 0 && accu < i) {
				ans += (i - accu);
				accu = i;
			}

			accu += list[i] - '0';
		}

		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}