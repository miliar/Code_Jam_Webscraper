#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 210;

int all, select;
double prob[MAX], table[2][MAX];

double force() {
	int ss[MAX], as[MAX];
	for (int i = 0; i < all; i++)
		ss[i] = i >= all-select;

	double ans = 0;
	do {
		table[0][0] = 1;

		int count = 0;
		bool c;
		for (int i = 0; i < all; i++) {
			if (ss[i] == 1) {
				count++;
				c = count & 1;
				for (int j = 0; j <= count; j++) {
					table[c][j] = 0;
					if (j > 0) table[c][j] += prob[i] * table[!c][j-1];
					if (j != count) table[c][j] += (1 - prob[i]) * table[!c][j];
				}
			}
		}
		if (table[c][select / 2] > ans) {
			ans = table[c][select / 2];
			for (int i = 0; i < all; i++)
				as[i] = ss[i];
		}
	} while(next_permutation(ss, ss+all));

	return ans;
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);
	for (nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%d%d", &all, &select);

		for (int i = 0; i < all; i++)
			scanf("%lf", &prob[i]);

		double brute = force();

		printf("Case #%d: %.10lf\n", nowCase, brute);
	}

	return 0;
}