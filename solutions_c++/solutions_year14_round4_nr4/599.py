#include <iostream>
#include <string>
#include <map>

using namespace std;

const int MAXM = 8, MAXN = 4;
int m, n;
string s[MAXM];
map<string, int> t[MAXN];
int ans, cnt;

void init()
{
	cin >> m >> n;
	for (int i = 0; i < m; ++i) cin >> s[i];
	ans = 0; cnt = 0;
}

int add(map<string, int> &t, const string &s)
{
	int tot = 0;
	for (int i = 0; i <= s.size(); ++i) {
		if (t[s.substr(0, i)]++ == 0) ++tot;
	}
	return tot;
}

void del(map<string, int> &t, const string &s)
{
	for (int i = 0; i <= s.size(); ++i) {
		--t[s.substr(0, i)];
	}
}

void dfs(int p, int sum)
{
	if (p == m) {
		if (sum > ans) ans = sum, cnt = 0;
		if (sum == ans) ++cnt;
		return;
	}
	for (int i = 0; i < n; ++i) {
		int x = add(t[i], s[p]);
		dfs(p + 1, sum + x);
		del(t[i], s[p]);
	}
}

int main()
{
	int dat;
	cin >> dat;
	for (int cas = 1; cas <= dat; ++cas) {
		init();
		dfs(0, 0);
		cout << "Case #" << cas << ": " << ans << " " << cnt << endl;
	}
}
