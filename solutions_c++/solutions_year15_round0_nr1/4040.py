// Problem A. Standing Ovation
#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d\n", &T);
	for (int ti = 1; ti <= T; ti++) {
		int m, sum = 0, ans = 0;
		static char s[1024];
		scanf("%d %s", &m, s);
		for (int i = 0; s[i]; i++) {
			int n = s[i] - '0';
			if (n > 0 && i > sum) {
				int t = i - sum;
				ans += t;
				sum += t;
			}
			sum += n;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
