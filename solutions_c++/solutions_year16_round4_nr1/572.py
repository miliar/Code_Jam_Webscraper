#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
typedef pair<int, int> pii;
const double eps = 1e-7;
const int maxn = 200 + 5;
int n, r, p, s;
int a[3], cnt;
char ans[1<<13];
inline void get(int &x)
{
	char ch = getchar();
	while (ch < '0' || ch > '9') ch = getchar();
	x = ch - '0';
	while (ch = getchar(), ch >= '0' && ch <= '9') x = 10 * x + ch - '0';
}
int ok()
{
	if (a[0] == p && a[1] == r && a[2] ==s) return 0;
	if (a[0] == r && a[1] == s && a[2] ==p) return 1;
	if (a[0] == s && a[1] == p && a[2] ==r) return 2;
	return -1;
}
void dfs(int x,int d)
{
	if(d < 0) return ;
	if(!d)
	{
		if (x == 0) ans[cnt++] = 'P';
		else if (x == 1) ans[cnt++] = 'R';
		else if (x == 2) ans[cnt++] = 'S';
	}
	dfs(x, d - 1);
	dfs((x + 1) % 3, d - 1);
}
void Sort(char *a, int l)
{
	if(l == 0) return ;
	Sort(a, l>>1);
	Sort(a + l, l>>1);
	int i = 0;
	while(a[i] == a[l + i]) i++;
	if(a[i] < a[l + i]) return ;
	for (int j = 0; j < l; j++) swap(a[j], a[l + j]);
}
void run()
{
	scanf("%d%d%d%d", &n, &r, &p, &s);
	a[0] = 1, a[1] = a[2] = 0;
	for (int i = 0; i < n ; i++)
	{
		int x = a[0] + a[2], y = a[0] + a[1], z = a[1] + a[2];
		a[0] = x;
		a[1] = y;
		a[2] = z;
	}
	int r = ok();
	if(r == -1)
	{
		puts("IMPOSSIBLE");
		return ;
	}
	memset(ans, 0, sizeof ans);
	cnt = 0;
	dfs(r, n);
	Sort(ans, 1 << n - 1);
	puts(ans);
}
int main()
{
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++)
	{
		printf("Case #%d: ", cas);
		run();
	}
	return 0;
}


