#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> MI;

typedef vector<bool> VB;

typedef vector<string> VS;

int check(string &s) {
	set<char> used;
	int c = s[0];
	for(int i = 0; i < s.size(); ++i) {
		if(c != s[i]) {
			if(used.find(s[i]) == used.end()) {
				used.insert(c);
				c = s[i];
			} else {
				return 0;
			}
		}
	}
	return 1;
}

int calc(MI &graph, VB &used, int pos, int left, string &s, VS &train) {
	if(left == 0) {
		return check(s);
	}
	int res = 0;
	bool done = false;
	for(int i = 0; i < graph[pos].size(); ++i) {
		if (not used[graph[pos][i]]) {
			used[graph[pos][i]] = true;
			string s2 = s;
			s2 += train[graph[pos][i]];
			res += calc(graph, used, graph[pos][i], left-1, s2, train);
			used[graph[pos][i]] = false;
			done = true;
		}
	}
	if (not done) {
		for(int i = 0; i < graph.size(); ++i) {
			if (not used[i]) {
				used[i] = true;
				string s2 = s;
				s2 += train[i];
				res += calc(graph, used, i, left-1, s2, train);
				used[i] = false;
			}
		}
	}
	return res;
}

int main() {
	int t;
	cin >> t;
	for(int tcas = 0; tcas < t; ++tcas) {
		int n;
		cin >> n;
		VS train(n);
		for(int i = 0; i < n; ++i) {
			string s;
			cin >> s;
			train[i] = s;
		}
		MI graph(n, VI(0));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (i != j) {
					if(train[j][0] == train[i][int(train[i].size())-1]) {
						graph[i].push_back(j);
					}
				}
			}
		}
		VB used(n,false);
		used[0] = true;
		string s = train[0];
		int res = calc(graph, used, 0, n-1, s, train);
		used[0] = false;
		for(int i = 1; i < n; ++i) {
			s = train[i];
			used[i] = true;
			res += calc(graph, used, i, n-1, s, train);
			used[i] = false;
		}
		cout << "Case #" << tcas+1 << ": " << res;
		cout << endl;
	}
}