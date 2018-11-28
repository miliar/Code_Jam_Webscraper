#include <cstdio>
#include <string>
#include <set>
#include <iostream>
using namespace std;

const int Maxm = 10;
const int Maxn = 5;

int t;
int m, n;
string s[Maxm];
int wh[Maxm];
int cnt[Maxn];
set <string> S[Maxn];
int mx, ways;

void Check()
{
	for (int i = 0; i < n; i++)
		if (!cnt[i]) return;
	for (int i = 0; i < m; i++) {
		S[wh[i]].insert("");
		for (int j = 0; j < s[i].length(); j++)
			S[wh[i]].insert(s[i].substr(0, j + 1));
	}
	int res = 0;
	for (int i = 0; i < n; i++) {
		res += S[i].size(); S[i].clear();
	}
	if (res > mx) { mx = res; ways = 0; }
	if (res == mx) ways++;
}

void Gen(int lvl)
{
	if (lvl == m) Check();
 	else for (int i = 0; i < n; i++) {
 			wh[lvl] = i; cnt[i]++;
 			Gen(lvl + 1);
 			cnt[i]--;
 		}
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &m, &n);
		for (int i = 0; i < m; i++)
			cin >> s[i];
		mx = 0;
		Gen(0);
		printf("Case #%d: %d %d\n", tc, mx, ways);
	}
	return 0;
}