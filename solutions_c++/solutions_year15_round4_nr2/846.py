#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <cassert>
#include <cmath>

#define INF 2000000000
#define MOD 1000000007
#define EPS 0.000000000001

using namespace std;

int n;
double t[100], rate[100];
double V, T;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		cin >> n >> V >> T;
		for (int i = 0; i < n; i++)
			cin >> rate[i] >> t[i];
		bool low = false, high = false;
		double eqs = 0;
		for (int i = 0; i < n; i++) {
			if (t[i] > T)
				high = true;
			else if (t[i]< T)
				low = true;
			else
				eqs += rate[i];
		}
		if (n == 1) {
			if (t[0] != T) {
				printf("IMPOSSIBLE\n");
				continue;
			}
			else {
				printf("%.8f\n", V / rate[0]);
				continue;
			}
		}
		if (n == 2) {
			if (eqs != 0) {
				printf("%.8f\n", V / eqs);
				continue;
			}
			else if (low && high) {
				printf("%.8lf\n", max(V * (T - t[1]) / (t[0] - t[1]) / rate[0], V * (T - t[0]) / (t[1] - t[0]) / rate[1]));
				continue;  
			}
			else {
				printf("IMPOSSIBLE\n");
				continue;
			}
		}
	}
	return 0;
}
