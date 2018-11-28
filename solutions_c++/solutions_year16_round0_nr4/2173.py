#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, m;

int main(){
	int T, K, C, S;
	cin >> T;
	for (int Te = 1; Te <= T; ++Te) {
		cout << "Case #" << Te << ":";
		cin >> K >> C >> S;
		if (K == S) {
			LL e = 1;
			for (int i = 1; i < C; ++i) e *= K;
			for (int i = 0; i < K; ++i)
				cout << ' ' << 1 + e * i;
			cout << endl;
		} else {
			cout << " IMPOSSIBLE" << endl;
		}
	}
}
