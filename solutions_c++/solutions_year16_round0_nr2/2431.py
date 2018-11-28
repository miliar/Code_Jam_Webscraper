#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;

string s;
map<string, int> d;
int T;
                         
void load() {
	cin >> s;
}

void solve(int tc) {
	d[s] = 0;
	queue<string> q;
	q.push(s);
	while (!q.empty()) {
		string t = q.front();
		q.pop();
		for (int i = 1; i <= (int)t.size(); ++i) {
			string tmp = t.substr(0, i);
			reverse(tmp.begin(), tmp.end());
			for (auto &c : tmp) {
				c ^= '+' ^ '-';
			}
			tmp += t.substr(i);
			if (d.count(tmp) == 0) {
				d[tmp] = d[t] + 1;
				q.push(tmp);
			}
		}
	}
	cout << "Case #" << tc << ": " << d[string(s.size(), '+')] << endl;		
}

void clear() {
	d.clear();
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		load();
		solve(tc);
		clear();
	}
	return 0;
}