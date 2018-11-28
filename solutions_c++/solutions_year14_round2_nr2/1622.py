#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sz(x) (int)(x).size()

typedef long long ll;

void solveOne(int t) {
	int a, b, k, res = 0;
	cin >> a >> b >> k;
	for(int i = 0;i < a;i++) {
		for(int j = 0;j < b;j++) {
			if((i & j) < k) res++;
		}
	}
	cout << "Case #" << t << ": " << res << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int tests;
	cin >> tests;
	for(int t = 1;t <= tests;t++) {
		solveOne(t);
	}
	return 0;
}
