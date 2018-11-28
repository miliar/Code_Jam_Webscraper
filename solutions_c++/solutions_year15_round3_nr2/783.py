#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (int)(b); i++)
#define REP(i, n) FOR(i, 0, n)
#define F first
#define S second
#define ZERO(x) memset(x, 0, sizeof (x))
typedef long long int ll;
typedef pair<int,int> par;

int k, l, s;
char strk[12]; // keyboard
char strl[12]; // target
char strs[12]; // actual
int a[12];

bool next_a()
{
	int i = 0;
	a[i]++;
	while (a[i] == k) {
		a[i++] = 0;
		if (i == s) return false;
		a[i]++;
	}
	return true;
}

void solve()
{
	ZERO(a);
	scanf("%d%d%d", &k, &l, &s);
	scanf("%s", strk);
	scanf("%s", strl);
	int MAX = 0, cur = 0, tot = 0;
	do {
		REP(i, s) strs[i] = strk[ a[i] ];
		int cnt = 0;
		REP(i, s-l+1) {
			if (memcmp(&strs[i], strl, l) == 0) cnt++;
		}
		MAX = max(MAX, cnt);
		cur += cnt;
		tot++;
	} while(next_a());
	double sol = cur;
	sol = MAX - sol/tot;
	printf("%.7f\n", sol);
}

int main()
{
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
