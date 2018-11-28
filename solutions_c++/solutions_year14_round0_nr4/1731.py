#include <algorithm>
#include <cstdio>
#include <cstring>
#define REP(i, n) for (i = 0; i < (n); i++)
#define REP1(i, n) for (i = 1; i <= (n); i++)
using namespace std;

const int N = 1000 +10;

bool flag[N];

int ans1, ans2, n, nowtd, tdnum;

double a[N], b[N];

bool cmp(double a, double b) {return a > b;}

void ri()
{
	int i;

	memset(flag, true, sizeof(flag));
	scanf("%d", &n);
	REP(i, n) scanf("%lf", &a[i]);
	REP(i, n) scanf("%lf", &b[i]);
	sort(a, a + n, cmp);
	sort(b, b + n, cmp);
	ans1 = 0;
	ans2 = 0;
}

bool nf(double x)
{
	int i, j = -1;

	REP(i, n) if (b[i] > x && flag[i]) j = i;
	if (j != -1)
	{
		flag[j] = false;
		return false;
	}
	REP(i, n) if (flag[i]) j = i;
	flag[j] = false;
	return true;
}

void solve()
{
	int i, j = n - 1;

	REP(i, n) ans1 += nf(a[i]);
	REP(i, n)
		if (a[n - 1 - i] > b[j])
		{
			ans2++;
			j--;
		}
}

void print() {printf("Case #%d: %d %d\n", nowtd, ans2, ans1);}

int main()
{
	scanf("%d", &tdnum);
	REP1(nowtd, tdnum)
	{
		ri();
		solve();
		print();
	}
	return 0;
}
