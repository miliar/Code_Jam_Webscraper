#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
#define y1 botva23
typedef long long int64;
typedef long double ld;

const int inf = 1000002013;
const ld eps = 1e-07;

int64 n, p;
int64 k;
bool a[100];

bool can(int64 x) {
	if (p == (k - 1LL))
		return true;

	int64 curless = x;
	int64 curmore = k - x - 1;
	
	for (int i = 0; i < n; ++i) {
		if (!a[i]) {
			if (curmore)
				return true;
			curless = (curless - 1LL) / 2LL;
		}
		else {
			if (!curmore)
				return false;
			curmore--;
			if (curless & 1) {
				curless = ((curless - 1LL) / 2LL) + 1LL;
				curmore = (curmore - 1) / 2LL;
			}
			else {
				curless = curless / 2LL;
				curmore = curmore / 2LL;
			}
		}
	}
	return true;
}

bool should(int64 x) {
	if (p == (k - 1LL))
		return true;

	int64 curless = x;
	int64 curmore = k - x - 1;
	
	for (int i = 0; i < n; ++i) {
		if (!a[i]) {
			if (!curless)
				return true;
			curless--;
			if (curmore & 1) {
				curmore = ((curmore - 1) / 2LL) + 1LL;
				curless = (curless - 1) / 2LL;
			}
			else {
				curmore = curmore / 2LL;
				curless = curless / 2LL;
			}
		}
		else {
			if (curless)
				return false;
			--curmore;
			if (curless > curmore) {
				curless = curmore + ((curless - curmore) / 2LL);
				curmore = 0;
			}
			else {
				curmore -= curless;
				curmore /= 2LL;
			}
		}
	}
	return true;
}

void solve() {	
	cin >> n >> p;
	--p;
	int64 tmp = n - 1;
	for (int i = 0; i < n; ++i) {
		if (p & (1LL << tmp)) {
			a[i] = false;
		}
		else a[i] = true;
		--tmp;
	}	
	k = (1LL << n);
	int64 l = 0;
	int64 r = k - 1LL;
	
	l = 0;
	r = k - 1LL;
	while (r - l > 2LL) {
		int64 m = (l + r) >> 1LL;
		if (should(m)) {
			l = m;
		}
		else r = m - 1;
	}
	for (int64 i = r; i >= l; --i)
		if (should(i)) {
			cout << i << " ";
			break;
		}



	l = 0;
	r = k - 1LL;
	while (r - l > 2LL) {
		int64 m = (l + r) >> 1LL;
		if (can(m)) {
			l = m;
		}
		else r = m - 1;
	}
	for (int64 i = r; i >= l; --i)
		if (can(i)) {
			cout << i << " ";
			break;
		}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int z = 1; z <= t; ++z) {
		printf("Case #%d: ", z);
		solve();
		cout << endl;
	}
	return 0;
}