#include <bits/stdc++.h>
#define fst first
#define snd second
#define pb push_back
#define endl '\n'

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long int64;


string get_state(const string &v, int k) {
	string ans;
	for (char c : v) ans.pb(c);
	for (int i = 0, j = k; i <= j; i++, j--) {
		swap(ans[i], ans[j]);
		if (i != j) ans[i] = ans[i] == '+' ? '-' : '+';
		ans[j] = ans[j] == '+' ? '-' : '+';
	}
	return ans;
}


int solve(string s) {
	string want;
	for (char c : s) want.pb('+');
	queue<string> q;
	map<string, int> dist;
	map<string, string> prev;
	dist[s] = 0;
	q.push(s);
	bool done = 0;
	while (!q.empty() && !done) {
		string from = q.front(); q.pop();
		// cout << "from: " << from << endl;
		for (int i = 0; i < from.size(); i++) {
			string to = get_state(from, i);
			// cout << "to: " << to << endl;
			if (dist.find(to) == dist.end()) {
				dist[to] = dist[from] + 1;
				prev[to] = from;
				q.push(to);
				if (to == want) {
					done = 1;
					break;
				}
			}
		}
	}
	// string curr = want;
	// vector<string> ans;
	// ans.pb(curr);
	// while (prev.find(curr) != prev.end()) {
	// 	ans.pb(prev[curr]);
	// 	curr = prev[curr];
	// }
	// for (int i = 0; i < ans.size(); i++)
	// 	cout << ans[ans.size() - i - 1] << endl;
	return dist[want];
}

int solve2(string s) {
	string want, neg;
	for (char c : s) {
		want.pb('+');
		neg.pb('-');
	}
	if (s == want) return 0;
	queue<string> q;
	map<string, int> dist;
	map<string, string> prev;
	dist[s] = 0;
	q.push(s);
	bool done = 0;
	while (!q.empty() && !done) {
		string from = q.front(); q.pop();
		if (from == neg) return dist[from] + 1;
		char pr = from[0];
		// cout << "from: " << from << endl;
		for (int i = 1; i < from.size() ; i++) {
			if (from[i] == pr) continue;
			string to = get_state(from, i-1);
			// cout << "to: " << to << endl;
			if (dist.find(to) == dist.end()) {
				dist[to] = dist[from] + 1;
				q.push(to);
				if (to == want) {
					done = 1;
					break;
				}
			}
			break;
		}
	}
	return dist[want];
}

int main () {
	ifstream fin("in_b.in");
	ofstream fout("ans_b.out");
	int t;
	fin >> t;
	for (int num_case = 1; num_case <= t; num_case++) {
		string s;
		fin >> s;
		fout << "Case #" << num_case << ": ";
		// int ans = solve(s);
		// assert(solve2(s) == ans);
		fout << solve2(s) << endl;
		// cerr << "got one\n";
	}
	return 0;
}