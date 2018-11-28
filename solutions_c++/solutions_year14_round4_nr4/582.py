#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <numeric>
#include <utility>
#include <functional>
#include <algorithm>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	char t[32];

	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int m, n;
		cin >> m >> n;
		vector<string> s;
		for (int i = 0; i < m; i++) {
			cin >> t;
			s.push_back(t);
		}

		map<int, int> z;

		int x = 1;
		for (int i = 0; i < m; i++) x *= n;
		for (int k = 0; k < x; k++) {
			vector<vector<int> > a(n, vector<int>());
			for (int i = 0, j = k; i < m; i++, j /= n)
				a[j % n].push_back(i);
			int ok = true;
			for (int i = 0; i < n; i++)
				if (a[i].size() == 0) {
					ok = false;
					break;
				}
			if (!ok) continue;
			int c = 0;
			for (int i = 0; i < n; i++) {
				set<string> ss;
				for (int j = 0; j < a[i].size(); j++) {
					const string &t = s[a[i][j]];
					for (int l = 1; l <= t.size(); l++)
						ss.insert(t.substr(0, l));
				}
				c += ss.size() + 1;
			}
			z[c] = z[c] + 1;
		}
		int ansx = 0, ansy = 0;
		for (map<int, int>::iterator it = z.begin(); it != z.end(); it++)
			ansx = it->first, ansy = it->second;

		printf("Case #%d: %d %d\n", ti, ansx, ansy);
	}

	return 0;
}
