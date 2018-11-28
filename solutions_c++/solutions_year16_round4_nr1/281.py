#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

vector<vector<int>> arrs[3];

int solve() {
 	int n, r, p, s;
 	scanf("%d%d%d%d", &n, &r, &p, &s);
 	vector<int> ans = {10};
 	for (int i = 0; i < 3; ++i) {
 	 	vector<int> numof(3);
 	 	for (int num: arrs[i][n]) {
 	 	 	numof[num]++;
 	 	}
 	 	if (numof[0] == p && numof[1] == r && numof[2] == s) {
 	 	 	ans = min(ans, arrs[i][n]);
 	 	}
 	}
 	if (ans[0] == 10) {
 	 	cout << "IMPOSSIBLE";
 	} else {
 	 	for (int num: ans) {
 	 	 	cout << "PRS"[num];
 	 	}
 	}
 	cout << "\n";
 	return 0;
}

int main() {
	//freopen(TASK_NAME ".in", "r", stdin);
	//freopen(TASK_NAME ".out", "w", stdout);

	arrs[0] = {{0}};
	arrs[1] = {{1}};
	arrs[2] = {{2}};

	//vector<int> beats = {1, 2, 0};

	for (int i = 1; i < 13; ++i) {
	 	for (int j = 0; j < 3; ++j) {
	 	 	int next = (j + 1) % 3;
	 	 	if (arrs[j][i - 1] < arrs[next][i - 1]) {
	 	 	 	vector<int> res;
	 	 	 	for (int num: arrs[j][i - 1]) {
	 	 	 	 	res.puba(num);
	 	 	 	}
	 	 	 	for (int num: arrs[next][i - 1]) {
	 	 	 	 	res.puba(num);
	 	 	 	}
	 	 	 	arrs[j].puba(res);
	 	 	} else {
	 	 	 	vector<int> res;
	 	 	 	for (int num: arrs[next][i - 1]) {
	 	 	 	 	res.puba(num);
	 	 	 	}
	 	 	 	for (int num: arrs[j][i - 1]) {
	 	 	 	 	res.puba(num);
	 	 	 	}
	 	 	 	arrs[j].puba(res);
	 	 	}
	 	}
	}

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; ++i) {
	 	cout << "Case #" << i + 1 << ": ";
	 	solve();
	}

	return 0;
}