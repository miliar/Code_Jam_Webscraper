#include <iostream>
#include <vector>
#include <cstdlib>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <map>
#include <sstream>
#include <list>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <set>
#include <utility>


using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int caseid = 1; caseid <= cases; caseid++) {
		map<int, int> rowid;
		int row1, row2;
		cin >> row1;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				int num;
				cin >> num;
				rowid[num] = i;
			}
		}
		cin >> row2;
		int ans = 0;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				int num;
				cin >> num;
				if (i == row2) {
					if (rowid[num] == row1) {
						if (ans == 0) {
							ans = num;
						} else {
							ans = -1;
						}
					}
				}
			}
		}
		cout << "Case #" << caseid << ": ";
		switch (ans) {
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case -1:
				cout << "Bad magician!" << endl;
				break;
			default:
				cout << ans << endl;
		}
	}
	return 0;
}
