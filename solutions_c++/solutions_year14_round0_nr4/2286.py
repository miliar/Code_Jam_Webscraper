#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

#define clr(a, x)  memset(a, x, sizeof(a))
#define REP(i, n)  for(int i = 0; i < (n); i++)
#define DEBUG

typedef long long LL;

const int N = 1005;
int T, n;
double a[N], b[N];

void solve() {
	cin >> T;
	REP(Case, T) {
		cin >> n;
		REP(i, n)  cin >> a[i];
		REP(i, n)  cin >> b[i];
		sort(a, a+n); sort(b, b+n);
		int pa, pb;
		pa = pb = n-1;
		int y = 0, z = 0;
		while(pa>=0 && pb>=0) {
			if(a[pa] > b[pb]) {
				--pa; --pb; ++y;
			}
			else  --pb;
		}
		pa = pb = n-1;
		while(pa>=0 && pb>=0) {
			if(b[pb] > a[pa]) {
				--pa; --pb; ++z;
			}
			else  --pa;
		}
		printf("Case #%d: %d %d\n", Case+1, y, n-z);
	}
}

int main() {
#ifdef DEBUG
	freopen("D-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	solve();
#ifdef DEBUG
	fclose(stdin);
	fclose(stdout);
#endif
	return  0;
}













