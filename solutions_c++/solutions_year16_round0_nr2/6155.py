#include <bits/stdc++.h>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

unordered_map<string, int> hm;

string solve() {
	string s;
	fin >> s;
	hm.clear();
	hm[s] = 0;
	int l = s.size();

	queue<string> q;
	q.push(s);
	while (q.size()) {
		string cur = q.front();
		q.pop();
		for (int i = 1; i <= l; i++) {
			string ns = "";
			for (int j = 0; j < i; j++)
				ns += (cur[j] == '-') ? '+' : '-';
			if (i < l) ns += cur.substr(i, l-i);

			if (hm.find(ns) == hm.end()) {
				hm[ns] = hm[cur] + 1;
				q.push(ns);
			}
		}
	}
	string gs = "";
	for (int i = 0; i < l; i++) gs += '+';
	return to_string(hm[gs]);
}

int main() {
	int x;
	fin >> x;
	for (int i = 0; i < x; i++)
		fout << "Case #" + to_string(i+1) + ": " + solve() + "\n";
}
