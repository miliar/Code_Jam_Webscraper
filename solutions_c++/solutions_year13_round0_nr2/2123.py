#include <cstdio>

using namespace std;

//#define SMALL
#define LARGE

int t, n, m;
int lawn[105][105], row_max[105];

bool check() {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (lawn[i][j] < row_max[i]) {
				for (int k = 0; k < n; ++k)
					if (lawn[k][j] > lawn[i][j])
						return false;
			}
		}
	}
	return true;
}

int main()
{
#ifdef SMALL
	freopen("B_small.in", "r", stdin);
	freopen("B_small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("B_large.in", "r", stdin);
	freopen("B_large.out", "w", stdout);
#endif

	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i) {
			row_max[i] = 0;
			for (int j = 0; j < m; ++j) {
				scanf("%d", &lawn[i][j]);
				if (lawn[i][j] > row_max[i])
					row_max[i] = lawn[i][j];
			}
		}
		printf("Case #%d: %s\n", Case, check() ? "YES" : "NO");
	}
	return 0;
}
