#include <cstdio>
#include <algorithm>
using namespace std;

const int Maxn = 1005;
const int Inf = 2000000000;

int t;
int n;
int a[Maxn];
bool er[Maxn];
int res;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]); er[i] = false;
		}
		res = 0;
		for (int i = 0; i < n; i++) {
			int mn = Inf, ind;
			for (int j = 0; j < n; j++)
				if (!er[j] && a[j] < mn) { mn = a[j]; ind = j; }
			int tol = 0, tor = 0;
			for (int j = 0; j < ind; j++)
				tol += !er[j];
			for (int j = ind + 1; j < n; j++)
				tor += !er[j];
			res += min(tol, tor);
			er[ind] = true;
		}
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}