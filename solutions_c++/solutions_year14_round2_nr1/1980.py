#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>
using namespace std;

int T, n;
vector<string> v;
string s;
map<int, int>::iterator it, it2;
map<int, int> mm;

vector<char> getCharVector(string s) {
	vector<char> chr;
	chr.push_back(s[0]);
	for (int i = 1; i < s.length(); i++)
		if (s[i] != s[i-1]) {
			chr.push_back(s[i]);
		}
	return chr;
}

map<int, int> getCharMap(string s) {
	map<int, int> m;
	m[0] = 1;
	for (int i = 1; i < s.length(); i++) {
		if (s[i] != s[i-1]) {
			m[m.size()]++;
		}
		else
			m[m.size() - 1]++;
	}
/*
	for (it = m.begin(); it != m.end(); it++)
		cout << (*it).second << ' ';
	cout << endl;
*/
	return m;
}

int main() {
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		printf("Case #%d: ", cc);

		cin >> n;
		v.clear();
		mm.clear();
		getline(cin, s);
		for (int i = 0; i < n; i++) {
			getline(cin, s);
			v.push_back(s);
		}

		if (v[0] == v[1]) {
			printf("0\n");
			continue;
		}

		vector<char> chr = getCharVector(v[0]);
		vector<char> chr2;
		map<int, int> m = getCharMap(v[0]);
		map<int, int> m2;

		int cnt = 0, diff = 0, idx = 0, ans = 214748364;
		bool tf = 0;
		for (int i = 1; i < v.size(); i++) {
			string t = v[i];
			chr2 = getCharVector(t);
			m2 = getCharMap(t);
			for (int j = 0; j < chr2.size(); j++)
				if (j >= chr.size() || chr2[j] != chr[j]) {
					tf = 1;
					break;
				}
			for (int j = 0; j < chr.size(); j++)
				if (j >= chr.size() || chr2[j] != chr[j]) {
					tf = 1;
					break;
				}

			if (tf)
				break;
			else {
				for (it = m.begin(), it2 = m2.begin(); it != m.end() && it2 != m2.end(); it++, it2++) {
					mm[(*it).first] = max(mm[(*it).first], abs((*it).second - (*it2).second));
				}	
				ans = min(ans, cnt);
			}
		}

		if (tf || idx >= chr.size() || ans == 214748364) {
			puts("Fegla Won");
		}
		else {
			ans = 0;
			for (it = mm.begin(); it != mm.end(); it++) {
				ans += (*it).second;
				// cout << (*it).first << ' ' << (*it).second << endl;
			}
			cout << ans << endl;
		}

	}

	return 0;
}