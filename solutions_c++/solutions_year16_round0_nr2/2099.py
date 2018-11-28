#include <bits/stdc++.h>
#define fst first
#define sec second
#define mp make_pair

using namespace std;

typedef long long LL;
typedef long double LD;

int f[1111][2];
char st[1111];

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
	memset(st, 0, sizeof(st));
	scanf("%s", st + 1);
	int len = strlen(st + 1);
	
	printf("Case #%d: ", cas);
	int cnt = 1;
	for (int i = 2; i <= len; i++)
		if (st[i] != st[i - 1])
			cnt++;
	if (st[1] == '-') printf("%d\n", f[cnt][0]);
	else printf("%d\n", f[cnt][1]);
}

int main() {
	f[1][0] = 1;
	f[1][1] = 0;
	for (int i = 2; i <= 1000; i++)
		if (i & 1)
		{
			f[i][0] = f[i - 1][1] + 1;
			f[i][1] = f[i - 1][1];
		}
		else 
		{
			f[i][0] = f[i - 1][0];
			f[i][1] = f[i - 1][0] + 1;
		}
	int T = getin();
	for (int i = 1; i <= T; i++)
		solve(i);
	return 0;	
}
