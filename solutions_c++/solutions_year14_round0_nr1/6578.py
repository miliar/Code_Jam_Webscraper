#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int main () {
	
	 freopen ("input.txt", "r", stdin);
	 freopen ("output.txt", "w", stdout);
	
	int p = 1, t, a[5][5];
	set <int> S;
	cin >> t;
	while (t--) {
		S.clear();
		int r1, r2, cnt = 0, res = -1;
		cin >> r1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				cin >> a[i][j];
				if (i + 1 == r1)
					S.insert(a[i][j]);
			}
		cin >> r2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				cin >> a[i][j];
				if (i + 1 == r2) {
				    if (S.count (a[i][j]) > 0)
				    	cnt++, res = a[i][j];
				}
			}
		if (cnt == 1) 
			printf ("Case #%d: %d\n", p++, res);
		else if (cnt > 1)
			printf ("Case #%d: Bad magician!\n", p++);
		else
			printf ("Case #%d: Volunteer cheated!\n", p++);
	}

	return 0;
}
