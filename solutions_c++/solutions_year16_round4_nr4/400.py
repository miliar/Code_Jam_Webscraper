#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <utility>
#include <memory.h>
#include <cassert>
#include <iterator>
#include <bitset>
#include <iomanip>
#include <complex>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>
#include <set>
#include <map>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define F first
#define S second
   
const int N = 11;

int n;     
int a[N][N];
char s[N][N];
bool go[N][(1 << 6)];

bool can(vector<int> &p) {
	memset(go, false, sizeof(go));
	int maxMask = (1 << n);
	go[0][0] = true;
	for (int i = 0; i < n; i++) {
		for (int mask = 0; mask < maxMask; mask++) {
			if (!go[i][mask]) continue;
			for (int j = 1; j <= n; j++) {
				if (a[p[i]][j] == 1 && (mask & (1 << (j - 1))) == 0) {
					go[i + 1][mask | (1 << (j - 1))] = true;
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int mask = 0; mask < maxMask; mask++) {
			if (!go[i][mask]) continue;
			int cnt = 0;
			for (int j = 0; j < n; j++) {
				if (a[p[i]][j + 1] == 1 && (mask & (1 << (j))) == 0) {
					++cnt;
				}
			}
			if (cnt == 0) return false;
		}
	}
	return true;
}

bool solve(int mask) {
	int id = -1;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			++id;
			if ((mask & (1 << id)) != 0) {
				a[i][j] = 1;
			} else {
				a[i][j] = 0;
			}
		}
	}
	vector<int> p;
	for (int i = 1; i <= n; i++) {
		p.pb(i);
	}
	bool fail = false;
	do {
		if (!can(p)) {
			fail = true;
			break;
		}
	} while (next_permutation(p.begin(), p.end()));	
	return !fail;
}

void solve(int test, int oo) {
	printf("Case #%d: ", test);
	scanf("%d\n", &n);
	for (int i = 1; i <= n; i++) gets(s[i] + 1);
	int maxMask = (1 << (n * n));
	int ans = (int)2e9;
	for (int mask = 0; mask < maxMask; mask++) {
		int now = 0;
		int id = -1;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				++id;
				if (s[i][j] == '1' && (mask & (1 << id)) == 0) {
					now = -1000;
					break;
				}
				if (s[i][j] == '0' && (mask & (1 << id)) != 0) {
					++now;
				}
			}
		}
		if (now < 0) continue;
		if (now > ans) continue;
		if (solve(mask)) {
			ans = min(ans, now);
		} 
	}
	printf("%d\n", ans);
}
              
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	srand(time(NULL));
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++) {
		solve(i, -1);
		cerr << i << "!" << endl;
	}
	return 0;
}
