#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int n;
int seq[1111];

void solve() {
	scanf("%d", &n);
	REP (i, n) {
		scanf("%d", &seq[i]);
	}
	int l = 0; int r = n-1;
	int ans = 0;
	REP(i, n) {
		int index; int h = INT_MAX;
		FOR (j, l, r) {
			if (seq[j]<h) {
				h = seq[j];
				index = j;
			}
		}
		if (index-l<r-index) {
			for (int j=index; j>l; j--) { swap(seq[j], seq[j-1]); ans++; }
			l++;
		}
		else {
			for (int j=index; j<r; j++) { swap(seq[j], seq[j+1]); ans++; }
			r--;
		}
	}
	printf("%d\n", ans);
}

int main() {
	int t; scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
