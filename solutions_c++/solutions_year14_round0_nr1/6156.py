#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		set<int> st;
		cout << "Case #" << i << ": ";
		int val, row, row1;
		cin >> row;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				int tmp = 0;
				cin >> tmp;
				if(j == row - 1) st.insert(tmp);
			}
		}
		cin >> row1;
		int cnt = 0;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				int tmp;
				cin >> tmp;
				if(j == row1 - 1 && st.count(tmp)) {
					val = tmp;
					cnt++;
				}
			}
		}
		if(cnt == 1) {
			cout << val << endl;
		} else if(cnt > 1) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}

