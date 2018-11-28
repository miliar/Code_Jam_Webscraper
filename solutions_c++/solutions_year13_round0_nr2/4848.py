#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main () {
	int n, m, t;
	scanf("%d", &t);
	bool is;
	vector <int> help, maxrow, maxcol;
	vector <vector <int> > lawn;
	for (int caser = 1; caser <= t; caser++) {
		scanf("%d %d", &n, &m);
		help.resize(m, 0);
		lawn.resize(n, help);
		maxcol.resize(m, 0); // maximum in a column
		maxrow.resize(n, 0); // maximum in a row
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &lawn [i] [j]);
				maxrow [i] = max (maxrow [i], lawn [i] [j]);
				maxcol [j] = max (maxcol [j], lawn [i] [j]);
			}
		}
		is = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if ((lawn [i] [j] != maxrow [i]) && (lawn [i] [j] != maxcol [j])) is = false;
			}
		}
		printf("Case #%d: ", caser);
		if (is) printf("YES\n");
		else printf("NO\n");
		maxcol.resize(0);
		maxrow.resize(0);
		lawn.resize(0);
	}
	return 0;
}