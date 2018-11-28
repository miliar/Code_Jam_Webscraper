#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; ++t) {
		int v1, v2;
		int c1[4][4], c2[4][4];
		vector<int> ch(16, 0);
		
		cin >> v1;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> c1[i][j];
				if (v1 == i + 1) ch[c1[i][j] - 1] ++;
			}
		}
		cin >> v2;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> c2[i][j];
				if (v2 == i + 1) ch[c2[i][j] - 1] ++;
			}
		}
		int cnt = 0;
		int ans = -1;
		for (int i = 0; i < 16; ++i) {
			if (ch[i] == 2) {
				++cnt;
				ans = i + 1;
			}
		}
		if (cnt == 1) {
			cout << "Case #" << t << ": " << ans << endl;
		} else if (cnt == 0) {
			cout << "Case #" << t << ": Volunteer cheated!" << endl;
		} else {
			cout << "Case #" << t << ": Bad magician!" << endl;
		}
		
	}
	
	return 0;
}
