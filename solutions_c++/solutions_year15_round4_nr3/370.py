#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ifstream fin("cs1.in");
ofstream fout("c.out");

unordered_map<string, int> wtoi;
vector<int> sent[200];
bitset<2400> wbs[200];

int addw(string s) {
	auto it = wtoi.find(s);
	if (it == wtoi.end()) {
		int cs = wtoi.size();
		wtoi[s] = cs;
		return cs;
	}
	return it->second;
}

void solve() {
	wtoi.clear();
	for (int i = 0; i < 200; i++) sent[i].clear(), wbs[i].reset();

	int n, res = 1<<30;
	fin >> n;
	string s;
	getline(fin, s);
	for (int i = 0; i < n; i++) {
		getline(fin, s);
		istringstream iss(s);
		vector<string> tv {istream_iterator<string>{iss}, istream_iterator<string>{}};
		for (string s : tv) {
			int id = addw(s);
			wbs[i][id] = 1;
			sent[i].push_back(id);
		}
	}
	int lim = 1<<(n-2), numw = wtoi.size();
	bitset<2400> E, F;
	for (int a : sent[0]) E[a] = 1;
	for (int a : sent[1]) F[a] = 1;

	for (int i = 0; i < lim; i++) {
		bitset<2400> l[2];
		l[0] = bitset<2400> (E.to_string());
		l[1] = bitset<2400> (F.to_string());
		for (int j = 0; j < n-2; j++)
				l[(i>>j) & 1] |= wbs[j+2];
		l[0] &= l[1];
		res = min(res, (int)l[0].count());
	}
	fout << res;
}

int main() {
	int a;
	fin >> a;
	for (int i = 0; i < a; i++) {
		fout << "Case #" << i+1 << ": ";
		solve();
	   	fout << '\n';
	}
}
