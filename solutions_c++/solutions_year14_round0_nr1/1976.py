#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <sstream>
using namespace std;

int cards[4][4];
int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int r1; scanf("%d", &r1); r1--;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &cards[i][j]);
			}
		}
		set<int> row(cards[r1], cards[r1+1]);
		int r2; scanf("%d", &r2); r2--;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &cards[i][j]);
			}
		}
		vector<int> ans;
		for (int i = 0; i < 4; ++i) {
			if (row.find(cards[r2][i]) != row.end())
				ans.push_back(cards[r2][i]);
		}


		printf("Case #%d: ", t);
		if (ans.size() == 1)
			printf("%d\n", ans[0]);
		else if (ans.size() == 0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
	}
	return 0;
}