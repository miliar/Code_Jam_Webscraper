#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	freopen("magictrick.in", "r", stdin);
	freopen("magictrick.out", "w", stdout);
	
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		int rs[2], ans = 0, nans = 0;
		map<int, bool> rows[2];
		cout << "Case #" << (i+1) << ": ";
		for (int m = 0; m < 2; m++) {
			cin >> rs[m];
			for (int j = 1; j <= 4; j++) { 
				for (int k = 0; k < 4; k++) {
					int v;
					cin >> v;
					if (j == rs[m]) rows[m][v] = 1;
				}
			}
		}
		for (map<int, bool>::iterator it = rows[0].begin(); it != rows[0].end(); ++it) {
			if (rows[1][it->first]) {
				ans = it->first;
				nans++;
			}
		}
		if (nans > 1) cout << "Bad magician!\n";
		else if (!nans) cout << "Volunteer cheated!\n";
		else cout << ans << "\n";
	}
	return 0;
}
