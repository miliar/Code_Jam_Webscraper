#include <cstdio>

const int SMAX = 1001;
static int S[SMAX] = {0};

bool solve(int i, int smax, int sum, int& inv)
{
	if (i - sum > 0)
		return false;

	if (i == smax)
		return true;

	int maxInv = 9 - S[i];
	for (int n = 0; n <= maxInv; n++) {
		if (solve(i + 1, smax, sum + S[i] + n, inv)) {
			inv += n;
			return true;
		}
	}

	return false;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		int smax;
		scanf("%d", &smax);

		char c;
		scanf("%c", &c);
		for (int j = 0; j <= smax; j++) {
			scanf("%c", &c);
			S[j] = c - '0';
		}

		int inv = 0;
		solve(0, smax, 0, inv);
		printf("Case #%d: %d\n", i + 1, inv);
	}

	return 0;
}
