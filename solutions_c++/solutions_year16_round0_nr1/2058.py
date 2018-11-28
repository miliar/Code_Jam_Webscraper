#include <bits/stdc++.h>
#define fst first
#define sec second
#define mp make_pair

using namespace std;

typedef long long LL;
typedef long double LD;

bool f[20];

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
	
	printf("Case #%d: ", cas);
	if (n == 0)
	{
		puts("INSOMNIA");
		return;
	}
	
	memset(f, 0, sizeof(f));
	bool flag = 1;
	int nx = 0;
	while (flag)
	{
		nx += n;
		for (int temp = nx; temp > 0; temp /= 10)
		{
			f[temp % 10] = 1;
		}
		
		flag = 0;
		for (int i = 0; i < 10; i++)
			if (!f[i]) flag = 1;
	}
	printf("%d\n", nx);
}

int main() {
	int T = getin();
	for (int i = 1; i <= T; i++)
		solve(i);
	return 0;	
}
