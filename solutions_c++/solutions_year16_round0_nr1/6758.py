#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif
}

void solveX(long long n) {	
	bool ok = false;
	int dig[10] = {0};
	if (!n) {
		cout << "INSOMNIA" << endl;
		return;
	}
	for (long long i = n; !ok; i += n) {
		char num[25];
		sprintf(num, "%lld", i);
		int len = strlen(num);
		for (int j = 0; j < len; j++) {
			dig[num[j] - '0'] = 1;
		}
		bool found = true;
		for (int j = 0; j < 10 && found; j++) {
			if (!dig[j]) found = false;
		}
		ok = found;
		if (ok) {
			cout << i << endl;
		}
	}
}

void solve() {
	long long n; cin >> n;
	solveX(n);
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
