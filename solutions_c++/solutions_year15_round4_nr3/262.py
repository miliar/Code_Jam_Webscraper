#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int t;
int n;
vector<string> s[222];
unordered_map<string,int> k1;
unordered_map<string,int> k2;
int p;

void haku(int k, int z) {
	if (z >= p) return;
	if (k == n) {
		p = min(p,z);
		return;
	}
	int u = z;
	unordered_set<string> lol;
	for (int j = 0; j < s[k].size(); j++) {
		if (lol.count(s[k][j])) continue;
		lol.insert(s[k][j]);
		if (k1[s[k][j]] == 0 && k2[s[k][j]]) u++;
		k1[s[k][j]]++;
	}
	haku(k+1, u);
	lol.clear();
	for (int j = 0; j < s[k].size(); j++) {
		if (lol.count(s[k][j])) continue;
		lol.insert(s[k][j]);
		k1[s[k][j]]--;
	}
	u = z;
	lol.clear();
	for (int j = 0; j < s[k].size(); j++) {
		if (lol.count(s[k][j])) continue;
		lol.insert(s[k][j]);
		if (k2[s[k][j]] == 0 && k1[s[k][j]]) u++;
		k2[s[k][j]]++;
	}
	haku(k+1, u);
	lol.clear();
	for (int j = 0; j < s[k].size(); j++) {
		if (lol.count(s[k][j])) continue;
		lol.insert(s[k][j]);
		k2[s[k][j]]--;
	}
}

void solve(int x) {
	cout << "Case #" << x << ": ";
	cin >> n;
	string r;
	getline(cin, r);
	for (int i = 0; i < n; i++) {
		s[i].clear();
		getline(cin, r);
		string u;
		for (int j = 0; j < r.size(); j++) {
			if (r[j] >= 'a' && r[j] <= 'z') {
				u = u+r[j];
			} else {
				s[i].push_back(u);
				u = "";
			}
		}
		if (u != "") s[i].push_back(u);
	}
	k1.clear();
	k2.clear();
	int a = 0;
	unordered_set<string> lol;
	for (int j = 0; j < s[0].size(); j++) {
		if (lol.count(s[0][j])) continue;
		lol.insert(s[0][j]);
		k1[s[0][j]]++;
	}
	lol.clear();
	for (int j = 0; j < s[1].size(); j++) {
		if (lol.count(s[1][j])) continue;
		lol.insert(s[1][j]);
		if (k1[s[1][j]]) a++;
		k2[s[1][j]]++;
	}
	p = 999999999;
	haku(2,a);
	cout << p << "\n";
}

int main() {
	cin >> t;
	for (int i = 0; i < t; i++) solve(i+1);
}
