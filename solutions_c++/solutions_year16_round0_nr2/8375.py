#include <bits/stdc++.h>
using namespace std;
unordered_map<string, int> vis;
string b;
vector<string> getAll(string a) {
	vector<string> ret;
	for (int i = 0; i < (int) a.size(); i++) {
		string s = a;
		for (int j = 0; j <= i; j++) {
			if (s[j] == '+')
				s[j] = '-';
			else
				s[j] = '+';
		}
		ret.push_back(s);
	}
	return ret;
}
void bfs(string s) {
	vis.clear();
	vis[s] = 0;
	queue<string> q;
	q.push(s);
	while (!q.empty()) {
		string a = q.front();
		if (a == b)
			return;
		q.pop();
		vector<string> v = getAll(a);
		for (int i = 0; i < (int) v.size(); i++)
			if (vis.find(v[i]) == vis.end()) {
				vis[v[i]] = vis[a] + 1;
				q.push(v[i]);
			}
	}
}
int main(int argc, char **argv) {
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		string a;
		cin >> a;
		b = "";
		for (int i = 0; i < (int) a.size(); i++)
			b += "+";
		bfs(a);
		cout << "Case #" << t << ": " << vis[b] << endl;
	}
}
