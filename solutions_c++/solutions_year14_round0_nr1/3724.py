#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int ROWS = 4;
const int COLS = 4;

void solve() {
	int ans;
	set<int> s1, s2;
	scanf("%d", &ans);
	--ans;
	for (int i = 0; i < ROWS; ++i) {
		for (int j = 0; j < COLS; ++j) {
			int x;
			scanf("%d", &x);
			if (i == ans) {
				s1.insert(x);
			}
		}
	}
	scanf("%d", &ans);
	--ans;
	for (int i = 0; i < ROWS; ++i) {
		for (int j = 0; j < COLS; ++j) {
			int x;
			scanf("%d", &x);
			if (i == ans) {
				s2.insert(x);
			}
		}
	}
	vector<int> out(4);
	vector<int>::iterator it = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), out.begin());
	int cnt = it - out.begin();
	if (cnt == 1) {
		printf("%d", *out.begin());
	} else if (cnt > 1) {
		printf("Bad magician!");
	} else {
		printf("Volunteer cheated!");
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
	return 0;
}