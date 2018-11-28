#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <sstream>
using namespace std;
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		int row, arr[4][4];
		vector<int>all;
		cin >> row;
		for(int i = 0; i<4; i++) {
			for(int j = 0; j<4; j++) {
				cin >> arr[i][j];
				if(i == row - 1) all.push_back(arr[i][j]);
			}
		}
		cin >> row;
		for(int i = 0; i<4; i++) {
			for(int j = 0; j<4; j++) {
				cin >> arr[i][j];
				if(i == row - 1) all.push_back(arr[i][j]);
			}
		}
		sort(all.begin(), all.end());
		bool mag = 1, cheat = 1, first = 1; int res;
		for(int i = 1; i<8; i++) {
			if(first && all[i] == all[i - 1]) cheat = 0, res = all[i], first = 0;
			else if(all[i] == all[i - 1]) {
				mag = 0;
				break;
			}
		}
		cout << "Case #" << tc << ": ";
		if(!mag) cout << "Bad magician!" << endl;
		else if(cheat) cout << "Volunteer cheated!" << endl;
		else cout << res << endl;
	}
	return 0;
}
