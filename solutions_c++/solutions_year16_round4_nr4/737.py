#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 30;
int n;
int pos[MAXN][MAXN];
int pos2[MAXN][MAXN];
char buf[MAXN];

bool check_correct() {
	vector<int> can;
	for (int i = 0; i < n; ++i) {
		vector<int> conc(n, 0);
		can.clear();
		for (int j = 0; j < n; ++j) {
			if (pos2[i][j]) {
				can.push_back(j);
			}
		}
		if (can.size() == 0) {
			return false;
		}
		for (int j = 0; j < can.size(); ++j) {
			for (int k = 0; k < n; ++k) {
				if (pos2[k][can[j]]) {
					conc[k] = 1;
				}
			}
		}
		int concs = 0;
		for (int j = 0; j < n; ++j) {
			concs += conc[j];
		}
		if (concs - 1 >= can.size()) {
			return false;
		}
	}
	return true;
}

void solve()
{
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> buf;
		for (int j = 0; j < n; ++j) {
			pos[i][j] = buf[j] - '0';
		}
	}
	int bestcost = n * n;
	for (int msk = 0; msk < (1 << (n * n)); ++msk) {
		int cost = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				pos2[i][j] = ((msk & (1 << (i * n + j))) != 0);
				if (pos2[i][j] == 0 && pos[i][j] != 0) {
					cost = -1e9;
				}
				cost += pos2[i][j] - pos[i][j];
			}
		}
		if (cost < 0) {
			continue;
		}
		if (check_correct() && cost < bestcost) {
			bestcost = cost;
		}
	}
	cout << bestcost << endl;
}

int main()
{
	int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}
