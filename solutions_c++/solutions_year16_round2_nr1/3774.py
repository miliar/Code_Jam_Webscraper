#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>
using namespace std;

string numstr[10] = {"ZERO", "ONE", "TWO","THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
map<string, string> m;

int next(string &org, int num, string &des)
{
	int i, j;

	if (org.size() < numstr[num].size())
		return 0;

	des.erase(des.begin(), des.end());

	i = 0, j = 0;
	while (i < numstr[num].size() && j < org.size()) {
		if (org[j] < numstr[num][i]) {
			des.push_back(org[j]);
			j++;
		}
		else if (org[j] > numstr[num][i])
			return 0;
		else {
			i++, j++;
		}
	}
	if (i < numstr[num].size())
		return 0;

	while (j < org.size()) {
		des = des + org[j];
		j++;
	}

	return 1;
}

int solve(string &src, int first, string &res)
{
	int ret;
	string dest;

	if (src.size() == 0) {
		return 1;
	}

	for(int i=first; i<10; ++i) {
		if(next(src, i, dest)) {
			res.push_back('0'+i);
			ret = solve(dest, i, res);
			if(ret == 1)
				return 1;
			res.pop_back();
		}
	}
	return 0;
}

int main()
{
	int tcase, i, ret;
	string s, res;

	for (i=0; i<10; ++i) {
		sort(numstr[i].begin(), numstr[i].end());
	}

	cin >> tcase;

	for (i=1; i<=tcase; ++i) {
		cin >> s;
		sort(s.begin(), s.end());

		res.erase(res.begin(), res.end());
		solve(s, 0, res);
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}
