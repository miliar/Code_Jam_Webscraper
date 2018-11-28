#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<iostream>
#include<cstdio>

using namespace std;

map<string, int> _enum;
int enumerate(string s)
{
	if (_enum.count(s))
		return _enum[s];
	int num = _enum.size();
	_enum[s] = num;
	return num;
}

int solve()
{
	_enum.clear();
	int n;
	cin >> n;
	vector<vector<int> > s(n);
	string line;
	getline(cin, line);
	for (int i=0;i<n;++i) {
		getline(cin, line);
		string word;
		for (int j=0;j<line.length();++j)
			if (line[j] == ' ') {
				s[i].push_back(enumerate(word));
				word = "";
			} else
				word += line[j];
		s[i].push_back(enumerate(word));
	}
	int best = _enum.size();
	for (int mask = 0; mask < (1<<(n-2)); ++mask) {
		vector<int> v(_enum.size(), 0);
		for (size_t i=0;i<s[0].size();++i)
			v[s[0][i]] |= 1;
		for (size_t i=0;i<s[1].size();++i)
			v[s[1][i]] |= 2;
		for (int i=0;i<n-2;++i) {
			int val = ((1<<i)&mask) ? 1 : 2;
			for (size_t j=0;j<s[i+2].size();++j)
				v[s[i+2][j]] |= val;
		}
		int cnt = 0;
		for (size_t i = 0; i <v.size(); ++i)
			cnt += v[i] == 3;
		best = min(best, cnt);
	}
	return best;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
		printf("Case #%d: %d\n", t, solve());
	return 0;
}
