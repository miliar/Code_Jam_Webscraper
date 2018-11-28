#include <map>
#include <set>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <fstream>
#include <iostream>
using namespace std;
int n, a[100010], w, ans, l, r, k, T, m, b[1010], c[1010], cnt;
char s[100][100];
void work()
{
	int sta = 0, tempcnt = 0;
	for (int i = 1; i <= n; i++)
		sta |= (1 << (a[i] - 1));
	if (sta != k) return;
	set <string> tri[5];
	for (int i = 0; i < 5; i++) tri[i].clear();
	for (int i = 1; i <= n; i++)
	{
		string temp;
		temp = "";
		l = a[i];
		r = strlen(s[i]);
		for (int j = 0; j < r; j++)
		{
			temp += s[i][j];
			if (tri[l].find(temp) == tri[l].end())
				tri[l].insert(temp);
		}
	}
	for (int i = 1; i <= m; i++) tempcnt += tri[i].size();
	if (tempcnt == ans) cnt++;
	if (tempcnt > ans) ans = tempcnt, cnt = 1;
	return;
}
int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		ans = cnt = 0;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < 100; i++) memset(s, 0, sizeof(s));
		k = (1 << m) - 1;
		for (int i = 1; i <= n; i++) scanf("%s", s[i]);
		for (int i = 1; i <= n; i++) a[i] = 1;
		a[n] = 0;
		while (1)
		{
			int now = n;
			while (a[now] == m && now > 0) a[now--] = 1;
			if (!now) break;
			a[now]++;
			work();
		}
		printf("Case #%d: %d %d\n", ++w, ans + m, cnt);
 	}
	return 0;
}


