#include <bits/stdc++.h>
#define fst first
#define sec second
#define mp make_pair

using namespace std;

typedef long long LL;
typedef long double LD;

int getin() {
	char ch;
	while (!isdigit(ch = getchar()) && ch != '-');
	int x = ch == '-' ? 0 : ch - '0';
	int opt = ch == '-' ? -1 : 1;
	while (isdigit(ch = getchar())) x = x * 10 + ch - '0';
	return x * opt;
}

void solve(int cas)
{
	int n = getin();
	int m = getin();
	int k = getin();
	
	printf("Case #%d:", cas);
	if ((n + m - 1) / m > k)
	{
		puts(" IMPOSSIBLE");
		return;
	}
	
	LL len = 1;
	for (int i = 1; i <= m; i++)
		len *= n;
	
	for (int i = 1; i <= n; i += m)	
	{
		LL temp = len / n, ans = 0;
		for (int j = i; j < min(i + min(m, n), n + 1); j++, temp /= n)
			ans += temp * (j - 1);
		printf(" %lld", ans + 1);
	}
	printf("\n");
}

int main() {
	int T = getin();
	for (int i = 1; i <= T; i++)
		solve(i);
	return 0;	
}
