#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int n, m;
set <string> good;
string bad;

pair <string, string> dummy() {
	if (good.count(bad))
		return make_pair("IMPOSSIBLE", "");
	string a;
	if (m == 1)
		a = "0";
	for (int i = 0; i < m - 1; i++)
		a += "1";
	string b;
	for (int i = 0; i < m; i++)
		b += "0?";
	return make_pair(a, b);
}

void solve(int t) {
	cin >> n >> m;
	good.clear();
	bad.clear();
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		good.insert(s);
	}
	cin >> bad;
	pair <string, string> ans = dummy();
	cout << "Case #" << t << ": " << ans.first << " " << ans.second << endl;
}

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++)
		solve(t);
}