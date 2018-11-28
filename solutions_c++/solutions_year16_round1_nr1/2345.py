#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int n = s.size();
		string ret = "";
		ret += s[0];
		for (int i = 1; i < n; i++) {
			if (s[i] < ret[0]) {
				ret += s[i];
			} else {
				ret  = s[i] + ret;
			}
		}

		/* solution */

		cout << "Case #" << t << ": " << ret << endl;
	}
}

