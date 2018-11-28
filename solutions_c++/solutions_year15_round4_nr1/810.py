#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair

int main() {
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int r, c;
		cin >> r >> c;
		vector<vector<char>> v(r, vector<char>(c));
		FOR(i, 0, r) FOR(j, 0, c) cin >> v[i][j];
		int count = 0;
		FOR(i, 0, r) FOR(j, 0, c) {
			int dx[] = {0, 1, 0, -1};
			int dy[] = {-1, 0, 1, 0};
			if (v[i][j] == '.') continue;
			int p = 0;
			if (v[i][j] == '^') p = 0;
			if (v[i][j] == '>') p = 1;
			if (v[i][j] == 'v') p = 2;
			if (v[i][j] == '<') p = 3;
			bool found[] = {false, false, false, false};
			FOR(z, 0, r) {
				if (z == i) continue;
				if (v[z][j] == '.') continue;
				if (z < i) found[0] = true;
				else found[2] = true;
			}
			FOR(s, 0, c) {
				if (s == j) continue;
				if (v[i][s] == '.') continue;
				if (s < j) found[3] = true;
				else found[1] = true;
			}
			if (found[p]) {
			} else {
				bool geht = false;
				FOR(k, 0, 4) {
					if (k == p) continue;
					if (found[k]) {
						geht = true;
						break;
					}
				}
				if (geht) {
					count++;
				} else {
					cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
					goto weiter;
				}
			}
		}
		cout << "Case #" << t+1 << ": " << count << endl;
weiter:
	int a = 0;
	}
	return 0;
}
