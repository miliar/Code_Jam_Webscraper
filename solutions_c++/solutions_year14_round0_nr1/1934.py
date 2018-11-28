#include <stdio.h>
#include <string.h>
#define REP(i, n) for (i = 0; i < (n); i++)
#define REP1(i, n) for (i = 1; i <= (n); i++)
using namespace std;

const int N = 4;

int nowtd, tdnum;
int a[N][N], cnt[N * N +1];

void init()
{
	memset(a, 0, sizeof(a));
	memset(cnt, 0, sizeof(cnt));
}

void solve()
{
	int i, j, m;

	scanf("%d", &m);
	REP(i, N) REP(j, N) scanf("%d", &a[i][j]);
	REP(j, N) cnt[a[m - 1][j]]++;

	scanf("%d", &m);
	REP(i, N) REP(j, N) scanf("%d", &a[i][j]);
	REP(j, N) cnt[a[m - 1][j]]++;
}

void print()
{
	int cnt_ans = 0, last, i;

	REP(i, N * N +1)
		if (cnt[i] == 2)
		{
			cnt_ans++;
			last = i;
		}
	printf("Case #%d: ", nowtd);
	if (cnt_ans == 0) printf("Volunteer cheated!");
	else if (cnt_ans == 1) printf("%d", last);
	else printf("Bad magician!");
	printf("\n");
}

int main()
{
	scanf("%d", &tdnum);
	REP1(nowtd, tdnum)
	{
		init();
		solve();
		print();
	}
	return 0;
}
