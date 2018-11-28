#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>
#include <numeric>

using namespace std;

struct Tour {
	int paper, rock, sciss;
	string way;

	Tour(int p = 0, int r = 0, int s = 0, string w = "") : paper(p), rock(r), sciss(s), way(w) {}
};

const int MAXN = 13;

Tour dp[MAXN][3];

Tour update(Tour a, Tour b) {
	int p = a.paper + b.paper;
	int r = a.rock + b.rock;
	int s = a.sciss + b.sciss;
	string w = min(a.way + b.way, b.way + a.way);
	return Tour(p, r, s, w);
}

int main() {
	dp[0][0] = Tour(1, 0, 0, "P");
	dp[0][1] = Tour(0, 1, 0, "R");
	dp[0][2] = Tour(0, 0, 1, "S");
	for (int i = 1; i < MAXN; ++ i) {
		for (int j = 0; j < 3; ++ j) {
			int k = (j + 1) % 3;
			dp[i][j] = update(dp[i - 1][j], dp[i - 1][k]);
		}
	}

	int task;
	scanf("%d", &task);
	for (int index = 1; index <= task; ++ index) {
		int n, p, r, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		int flag = -1;
		for (int i = 0; i < 3; ++ i) {
			if (dp[n][i].paper == p && dp[n][i].rock == r && dp[n][i].sciss == s) {
				flag = i;
				break;
			}
		}
		printf("Case #%d: ", index);
		if (flag == -1) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%s\n", dp[n][flag].way.c_str());
		}
	}
	return 0;
}

