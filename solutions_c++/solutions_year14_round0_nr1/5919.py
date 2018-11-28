#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

vector<int> getRow() {
	vector<int> res;
	int x, target_row;
	scanf("%d", &target_row);
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			scanf("%d", &x);
			if (i == target_row - 1) {
				res.push_back(x);
			}
		}
	}
	return res;
}

int main() {
//	freopen("gcj1.in", "r", stdin);
//	freopen("gcj1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		vector<int> a = getRow();
		vector<int> b = getRow();
		int res = 0;
		int count = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[i] == b[j]) {
					count++;
					res = a[i];
				}
			}
		}
		if (count == 0) {
			printf("Volunteer cheated!\n");
		}
		else if (count == 1) {
			printf("%d\n", res);
		}
		else {
			printf("Bad magician!\n");
		}
	}
}