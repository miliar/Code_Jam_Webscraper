// Problem A. Oversized Pancake Flipper
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char s[2000];

int main(int argc, char *argv[])
{
	int T, k;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		scanf("%s %d", s, &k);
		int n = strlen(s), ans = 0;
		for (int i = 0; i < n - k + 1; i++)
			if (s[i] == '-') {
				for (int j = 0; j < k; j++)
					s[i + j] = s[i + j] == '-' ? '+' : '-';
				ans++;
			}
		bool ok = true;
		for (int i = n - k; i < n; i++)
			if (s[i] == '-') {
				ok = false;
				break;
			}
		if (ok)
			printf("Case #%d: %d\n", ti, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", ti);
	}

	return 0;
}
