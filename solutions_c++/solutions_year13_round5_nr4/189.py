#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>

#define MAX_LENGTH 200

using namespace std;

char str[MAX_LENGTH + 10];
double dp[1 << 20];

long long pow2ll(int k)
{
	return 1LL << k;
}

int solve_problem(int num_case)
{
	int n = 0;

	if (fgets(str, sizeof(str), stdin) == NULL)
		return 1;

	while (str[n] != 0)
		++n;
	--n;

	int mask = 0;
	for (int i = 0; i < n; i++)
		if (str[i] == 'X')
			mask |= 1 << i;

	fill(dp, dp + (1 << n), 0);
	dp[(1 << n) - 1] = 0.0;
	for (int i = (1 << n) - 2; i >= mask; i--)
		if ((i & mask) == mask) {
			int num_set = 0;
			int y = i;
			while (y > 0) {
				y &= y - 1;
				++num_set;
			}
			dp[i] = 0;
			for (int j = 0; j < n; j++) {
				int k = j;
				int l;
				for (l = 0; l < n; l++) {
					if ((i & (1 << k)) == 0)
						break;
					k = (k + 1) % n;
				}
				dp[i] += (n - l) + dp[i | (1 << k)];
			}
			dp[i] /= n;
			//printf("i=%d\n", i);
		}
	//printf("n=%d\n", n);

	printf("Case #%d: %.10lf\n", num_case, dp[mask]);

	return 0;
}

int main(int argc, char *argv[])
{
	const char *filenames[] = {
		"b.in",
		"b.out",
	};
	int num_tests;

	for (int i = 1; i < argc && i <= 2; i++)
		filenames[i - 1] = argv[i];

	if (freopen(filenames[0], "rt", stdin) == NULL) {
		fprintf(stderr, "Could not reopen stdin\n");
		return 1;
	}
	if (freopen(filenames[1], "wt", stdout) == NULL) {
		fprintf(stderr, "Could not reopen stdout\n");
		return 1;
	}

	if (fgets(str, sizeof(str), stdin) == NULL)
		return 1;
	num_tests = atoi(str);
	for (int i = 0; i < num_tests; i++)
		solve_problem(i + 1);

	return 0;
}
