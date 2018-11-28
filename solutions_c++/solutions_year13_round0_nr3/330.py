#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <functional>
using namespace std;

/*
typedef map<pair<int, int>, int> item;
typedef vector<item> table;
table m;
vector<int> d, s;
vector<string> lookup;

inline pair<int, int> swapped(int a, int b) {
	if (a > b) swap(a, b);
	return make_pair(a, b);
}

void rec(int n, int q, int k) {
	if (k >= q) {
		string res;
		for (int i = 0; i < 2 * n - 1; ++i)
			res += char(s[i] + '0');
		lookup.push_back(res);
		return;
	}
	vector<int> old_s = s;
	for (int st = !k; st < 10; ++st) {
		d[k] = d[n - 1 - k] = st;
		bool f = true;
		for (int i = 0; i < 2 * n - 1; ++i) {
			for (item::iterator it = m[i].begin(), iend = m[i].end(); it != iend; ++it) {
				if (max(it->first.first, it->first.second) == k) {
					int delta = it->second * d[it->first.first] * d[it->first.second];
					s[i] += delta;
					if (s[i] >= 10) { f = false; break; }
				}
			}
			if (!f) break;
		}
		if (f) rec(n, q, k + 1);
		s = old_s;
	}
}*/

void pad(string & s) {
	s = string(101-s.size(), '0') + s;
}

int main() {
	/*for (int n = 1; n <= 51; ++n) {
		vector<int> co(n);
		const int q = n / 2 + n % 2;
		for (int i = 0; i < q; ++i)
			co[i] = co[n - 1 - i] = i;
		m = table(2 * n - 1);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				++m[i + j][swapped(co[i], co[j])];
		d = vector<int>(n);
		s = vector<int>(2 * n - 1);
		rec(n, q, 0);
		cout << n << endl;
	}
	ofstream fout("lookup.txt");
	for (int i = 0, ilen = lookup.size(); i < ilen; ++i)
		fout << lookup[i] << endl;
	cout << lookup.size() << endl;*/

	ifstream look("lookup.txt");
	const int magic = 46228;
	vector<string> lookup(magic);
	for (int i = 0; i < magic; ++i) {
		look >> lookup[i];
		pad(lookup[i]);
	}

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N;
	fin >> N;
	for (int cas = 0; cas < N; ++cas) {
		fout << "Case #" << cas + 1 << ": ";
		string a, b;
		fin >> a >> b;
		pad(a);
		pad(b);
		int c = 0;
		for (int i = 0, ilen = lookup.size(); i < ilen; ++i)
			if (a <= lookup[i] && lookup[i] <= b)
				++c;
		fout << c << endl;
	}
}