#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector<LL > VLL;
typedef vector<string> VS;

const LL MAX_VAL = 100000000000000L;

char buf[16];
VLL vals;

int main() {
	int tcs;
	cin >> tcs;
	//process test cases
	for (int tc = 0; tc < tcs; ++tc) {
		LL res = 0;
		int na;
		cin >> na;
		VS vs, vs1;

		for (int i = 0; i < na; ++i) {
			string val;
			cin >> val;
			vs.push_back(val);

			for (int j = 1; j < val.size(); ) {
				if (val[j] == val[j-1]) val.erase(j, 1);
				else ++j;
			}

			vs1.push_back(val);
			//cout << val << endl;
		}

		if (vs1[0] == vs1[1]) {
/*
			for (int j = 1; j < min(vs[0].size(), vs[1].size()); ) {
				if (vs[0][j-1] == vs[1][j-1] && vs[0][j] != vs[1][j]) {
					++res;
				} else ++j;
			}
*/
			int i = 0, j = 0;
			for (; i < vs[0].size() && j < vs[1].size(); ++i, ++j) {
				if (vs[0][i] != vs[1][j]) {
					++res;
					if (vs[0][i] != vs[0][i-1]) --i;
					else --j;
				}
			}
			res += (vs[0].size() - i) + (vs[1].size() - j);
			cout << "Case #" << tc + 1 << ": " << res << endl;
		} else {
			cout << "Case #" << tc + 1 << ": " << "Fegla Won" << endl;
		}

	}

	return 0;
}
