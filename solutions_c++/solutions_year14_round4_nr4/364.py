#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define ll long long
#define pb push_back 
#define mp make_pair
#define FOR(x, l, r) for(x = (l); x <= (r); x++)
#define FORD(x, r, l) for(x = (r); x >= (l); x --)
using namespace std;
int n, m, ans1, ans2, tmp, a[100];
set<string> pp[100];
char st[100][100];
string tmps;
void dfs(int i)
{
	int j, l;
	if (i > n) {
		for (j = 1; j <= m; j ++) pp[j].clear();
		for (j = 1; j <= n; j ++) {
			tmps = "";
			for (l = 0; l < strlen(st[j]); l ++) {
				tmps = tmps + st[j][l];
				pp[a[j]].insert(tmps);
			}
		}
		tmp = 0;
		for (j = 1; j <= m; j ++) 
			if (pp[j].size()) tmp += pp[j].size();
			else return;
		if (tmp > ans1) ans1 = tmp, ans2 = 1;
		else if (tmp == ans1) ans2 ++;
		return;
	}
	for (j = 1; j <= m; j ++) {
		a[i] = j;
		dfs(i + 1);
	}
}
int main()
{
	int tt, cas = 0, i;
	freopen("input.txt", "r", stdin);
	freopen("output", "w", stdout);
	cin >> tt;
	while (tt --) {
		cin >> n >> m;
		FOR(i, 1, n) scanf("%s", st[i]);
		ans1 = 0; ans2 = 0;
		dfs(1); 
		printf("Case #%d: ", ++cas);
		cout << ans1 + m<< " " << ans2 << endl;
	}
	return 0;
}