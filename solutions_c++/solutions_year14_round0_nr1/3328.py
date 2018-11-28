#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>

using namespace std;

void solve(int cs) {
	int f, s;
	int a[5][5], b[5][5];
	scanf("%d", &f);
	for (int i = 1; i <= 4; i++) for (int j = 1; j <= 4; j++) scanf("%d", &a[i][j]);
	scanf("%d", &s);
	for (int i = 1; i <= 4; i++) for (int j = 1; j <= 4; j++) scanf("%d", &b[i][j]);
	set<int> Q, R;
	for (int i = 1; i <= 4; i++) Q.insert(a[f][i]);
	for (int i = 1; i <= 4; i++) {
		if (Q.find(b[s][i]) != Q.end()) R.insert(b[s][i]);
	}
	if (R.size() == 0) {
		printf("Case #%d: Volunteer cheated!\n", cs);
		return;
	}
	if (R.size() > 1) {
		printf("Case #%d: Bad magician!\n", cs);
		return;
	}
	printf("Case #%d: %d\n", cs, *R.begin());
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}