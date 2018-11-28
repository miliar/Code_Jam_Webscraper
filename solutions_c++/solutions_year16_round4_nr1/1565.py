#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <iomanip>
#include <bitset>
#include <string>
#include <sstream>
using namespace std;

const double epsilon  = 1e-9;
typedef long long ll;
typedef long double ld;

int main() {
	freopen("google2.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for (int testCounter = 1; testCounter <= numTests; testCounter++) {
		printf("Case #%d: ", testCounter);

		int n;
		cin >> n;

		int p, r, s;
		cin >> r >> p >> s;
		string solutions[] = {"PR", "RS", "PS", "PRPS", "PRRS", "PSRS", "PRPSPRRS", "PRPSPSRS", "PRRSPSRS"};
		bool found = false;
		for (int i = 0; i < 9; i++) {
			int rcnt = 0;
			int pcnt = 0;
			int scnt = 0;
			for (int j = 0; j < solutions[i].size(); j++) {
				rcnt += solutions[i][j] == 'R';
				pcnt += solutions[i][j] == 'P';
				scnt += solutions[i][j] == 'S';
			}

			if (rcnt == r && pcnt == p && scnt == s) {
				cout << solutions[i] << endl;
				found = true;
				break;
			}
		}
		if (!found) cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
