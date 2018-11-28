#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main() {
	int T;
	int row;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> row;
		int col[4];
		vector<int> list;
		for (int j=0; j < 4; ++j) {
			scanf("%d %d %d %d\n", &col[0], &col[1], &col[2], &col[3]);
			if (j != row -1) {
				continue;
			}
			for (int k = 0; k < 4; k++) {
				list.push_back(col[k]);
			}
		}

		cin >> row;
		int duplication_cnt = 0;
		int ans;
		for (int j = 0; j < 4; ++j) {
			scanf("%d %d %d %d\n", &col[0], &col[1], &col[2], &col[3]);
			if (j != row - 1) {
				continue;
			}
			for (int idx = 0; idx < list.size(); ++idx) {
				for (int k = 0; k < 4; k++) {
					if (list[idx] == col[k]) {
						ans = list[idx];
						duplication_cnt++;
					}
				}
			}
		}

		string ret;
		if (duplication_cnt == 0) {
			ret = "Volunteer cheated!";
		} else if (duplication_cnt == 1) {
			ret = to_string(ans);
		} else {
			ret = "Bad magician!";
		}

		printf("Case #%d: %s\n", i+1, ret.c_str());

	}
	
}
