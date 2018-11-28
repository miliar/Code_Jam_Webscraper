#include <iostream>
#include <string>
#include <set>
#include <algorithm>


using namespace std;

const int N = 110, M = 1010;
int n, m;
string s[M];
int ans, cnt;
int a[N];
set<string> z[N];

void very() {
	int tmp = 0;
	for (int i = 0; i < n; i++)
		z[i].clear();
	for (int i = 0; i < m; i++) {
		z[a[i]].insert(" ");
		for (int j = 0; j < s[i].length(); j++) 
			z[a[i]].insert(s[i].substr(0, j + 1));
	}
	for (int i = 0; i < n; i++)
		tmp += z[i].size();
//	cout << tmp << ' ' << ans << ' ' << cnt << endl;
	
	if (tmp == ans) {
		cnt++;
	//	for (int i = 0; i < m; i++) cout << a[i]; cout << endl;
	}
	else
	if (tmp > ans)
		ans = tmp, cnt = 1;
}

void dfs(int p) {
	if (p == m) {
		very();
		return ;
	}
	for (int i = 0; i < n; i++) {
		a[p] = i;
		dfs(p + 1);
	}
}

void solve() {
	cin >> m >> n;
	for (int i = 0; i < m; i++) cin >> s[i];
	ans = 0;
	cnt = 0;
	dfs(0);
	cout << ans << ' ' << cnt;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cerr << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << "Done" << endl;
	}
}