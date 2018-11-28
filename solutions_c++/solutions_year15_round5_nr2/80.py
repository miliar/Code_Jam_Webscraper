#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

const int MAXN = 10000;

int n, k;
int s[MAXN];
int du[MAXN];
int dd[MAXN];
int ss;


int solve() {
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n - k + 1; ++i)
		scanf("%d", &s[i]);
	for (int i = 0; i < n; ++i)
		du[i] = 0, dd[i] = 0;
	for (int i = n - k - 1; i >= 0; --i) {
		int dt = s[i] - s[i + 1];
		du[i] = max(0, du[i + k] - dt);
		dd[i] = min(0, dd[i + k] - dt);
	}
	ss = s[0];
	int mx = 0;
	for (int i = 0; i < k; ++i) {
		ss += dd[i], du[i] -= dd[i], mx = max(mx, du[i]);
	}
	ss += 1000000 * k;
	ss %= k;
//	cerr << mx << "\n";
	int sum = 0;
	for (int i = 0; i < k; ++i)
		sum += mx - du[i];
	if (sum >= ss)
		return mx;
	else
		return mx + 1;
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; ++i)
		printf("Case #%d: %d\n", i, solve());
	return 0;
}


