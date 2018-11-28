#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int t;
string s, res;

int main() {
	freopen("A-large.in", "r", stdin); freopen("output.out", "w", stdout);

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s;
		res.clear();
		res.push_back(s[0]);

		for (int j = 1; j < s.size(); ++j)
			if (s[j] >= res[0])
				res = s[j] + res;
			else
				res += s[j];

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}