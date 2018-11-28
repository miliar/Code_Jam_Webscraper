#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long LL;



int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int caseID = 1; caseID <= T; ++caseID) {
		LL N, M;
		cin >> N;
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", caseID);
			continue;
		}
		M = 0;
		bool vis[10] = { 0 };
		int visNum = 0;
		while (visNum < 10) {
			M += N;
			LL a = M;
			while (a > 0) {
				int v = a % 10;
				if (!vis[v]) ++visNum;
				vis[v] = true;
				a /= 10;
			}
		}
		printf("Case #%d: %lld\n", caseID, M);
	}
}