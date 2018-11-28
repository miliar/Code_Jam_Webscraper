#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstring>
#include <set>
#include <limits.h>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif

	int tc = 0, n = 0, m = 0, c = 1, min = INT_MAX, minr = 0, countr = 0,
			countc = 0, minc = 0;
	vector<vector<int> > v;
	bool ro = true, co = true;
	cin >> tc;

	while (tc--) {
		cin >> n >> m;
		v.resize(n, vector<int>(m));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> v[i][j];
			}

		}

		while (true) {

			int k = 0;
			while (k < (int) v.size()) {
				if (v[k].empty()) {
					v.erase(v.begin() + k);
					continue;
				}
				k++;
			}

			if (v.empty())
				break;
			countc = 0, countr = 0, co = true, ro = true, min = INT_MAX, minr =
								0, minc = 0;
			for (unsigned int i = 0; i < v.size(); i++) {

				for (unsigned int j = 0; j < v[0].size(); j++) {
					if (min > v[i][j]) {
						minr = i;
						minc = j;
						min = v[i][j];
					}

				}
			}
			for (unsigned int i = 0; i < v[minr].size(); i++) {
				if (v[minr][i] == min)
					countr++;
			}

			if (countr != (int) v[minr].size())
				ro = false;

			for (unsigned int i = 0; i < v.size(); i++) {
				if (v[i][minc] == min)
					countc++;
			}

			if (countc != (int) v.size())
				co = false;

			if (!ro && !co) {
				cout << "Case #" << c << ": " "NO" << endl;
				break;
			}

			if (co) {
				for (unsigned int i = 0; i < v.size(); i++) {
					v[i].erase(v[i].begin() + minc);
				}
				continue;
			} else if (ro) {
				v.erase(v.begin() + minr);
				continue;
			}


		}
		if (v.size() == 0)
			cout << "Case #" << c << ": " "YES" << endl;
		if (!v.empty())
			v.clear();
		c++;
	}

	return 0;
}
//By : mohamed waleed
