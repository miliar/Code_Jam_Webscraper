#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int nTest;
int n, m;
string S[10];
int f[10][10];

int maxNode, countMax;
int dis[10];
void attempt(int i) {
	if (i == n) {
		int cNode = 0;
		for (int i = 0; i < m; i++) {
			int tNode = 1;
			for (int j = 0; j < n; j++) {
				if (dis[j] == i) {
					tNode += S[j].length();
					int maxPref = 0;
					for (int jj = 0; jj < j; jj++)
						if (dis[jj] == i)
							maxPref = max(maxPref, f[jj][j]);
					tNode -= maxPref;
				}
			}
			if (tNode == 1) return;
			cNode += tNode;
		}
		if (cNode > maxNode) {
			maxNode = cNode;
			countMax = 1;
		}
		else if (cNode == maxNode)
			countMax++;
		return;
	}
	for (int j = 0; j < m; j++) {
		dis[i] = j;
		attempt(i + 1);
	}
}

int main() {

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("O.txt", "w", stdout);

	cin >> nTest;
	for (int test = 1; test <= nTest; test++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> S[i];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int &k = f[i][j];
				for (k = 0; k < S[i].length() && k < S[j].length() && S[i][k] == S[j][k]; k++);
			}
		}

		maxNode = 0;
		countMax = 0;
		attempt(0);

		printf("Case #%d: %d %d\n", test, maxNode, countMax);
	}

	return 0;
}