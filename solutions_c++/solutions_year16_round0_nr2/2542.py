#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)

map<string, int> mem;

string rev(string s, int i) {
	for (int j = 0; j + j <= i; j++)
		swap(s[j], s[i - j]);
	for (int j = 0; j <= i; j++)
		s[j] = '+' - s[j] + '-';
	return s;
}

queue<string> Q;

void solve(int cnt) {
	cout << "Case #" << cnt << ": ";
	string s;
	cin >> s;
	cout << mem[s] << endl;
}

int n;

int main() {
	mem.clear();
	string s;
	FOR(i, 1, 10) {
		s += '+';
		mem[s] = 0;
		Q.push(s);
	}
	while (!Q.empty()) {
		s = Q.front();
		Q.pop();
		for (int j = 0; j < s.length(); j++) {
			string t = rev(s, j);
			if (!mem.count(t)) {
				mem[t] = mem[s] + 1;
				Q.push(t);
			}
		}
	}
	cin >> n;
	FOR(i, 1, n)
		solve(i);
}