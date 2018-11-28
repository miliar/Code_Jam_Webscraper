#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) {
		int m, cnt = 0, ans = 0;
		char s[1500];
		scanf ("%d %s", &m, s);
		for (int j = 0; j <= m; j++) {
			if (s[j] - '0' > 0 && j > cnt) {
				ans += j - cnt;
				cnt = j;
			}
			cnt += s[j] - '0';
		}
		printf ("Case #%d: %d\n", i, ans);
	}
	return 0;
}
