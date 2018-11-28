#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<limits.h>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>

using namespace std;

int p[10001], n;
int solve() {
	int res = p[0];
	for(int cakes = 1; cakes < p[0]; ++ cakes) {
		int extra = 0;
		for(int i = 0; i < n && p[i] > cakes; ++ i)
			extra += ceill((p[i] - cakes) / (double)cakes);
		res = min(res, extra + cakes);
	}
	return res;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin >> T;
	for(int t = 1; t <= T; ++ t) {
		cin >> n;
		for(int i = 0; i < n; ++ i) cin >> p[i];
		sort(p, p + n); reverse(p, p + n);
		int res = solve();
		printf("Case #%d: %d\n", t, res);
	}
}