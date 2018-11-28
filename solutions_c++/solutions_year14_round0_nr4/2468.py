#include <cstdio>
#include <algorithm>
#define RI(a) scanf("%d", &(a))
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
using namespace std;
int main() {
	int ttt, tt = 0;
	RI(ttt);
	while (tt++ < ttt) {
		printf("Case #%d: ", tt);
		int n;
		double a[1000], b[1000];
		RI(n);
		REP(i,n)
			scanf("%lf", &a[i]);
		sort(a, a + n);
		REP(i,n)
			scanf("%lf", &b[i]);
		sort(b, b + n);
		int j = 0, ans = n, an = 0;
		REP(i,n)
		{
			while (j < n && a[i] > b[j])
				j++;
			if (j != n)
				ans--,j++;
			else
				break;
		}
		j=0;
		REP(i,n)
			if (a[i] > b[j])
				an++,j++;
		printf("%d %d\n", an, ans);

	}
}
