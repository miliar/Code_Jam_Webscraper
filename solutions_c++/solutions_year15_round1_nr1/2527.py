#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define ll long long
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
int m[1111];
int n;
bool ok(int v) {
	int curr = m[0];
	for(int k = 1; k < n; k++) {
		curr = max(0, curr-v);
		if(curr > m[k])
			return false;

		curr = m[k];
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		scanf("%d", &n);
		REP(i, n) scanf("%d", m+i);
		int ans1 = 0, sum = 0;
		REP(i, n) if(i > 0 && m[i] < m[i-1]) ans1 += m[i-1]-m[i];
		REP(i, n) sum += m[i];
		int ans2 = 0;
		int l = 0, r = sum+1;
		while(l < r) {
			int mid = (l+r)/2;
			if(ok(mid)) {
				r = mid;
			} else {
				l = mid+1;
			}
		}
		bool run = false;
		REP(i, n) {
			ans2 += min(m[i-1], l);
		}
		printf("Case #%d: %d %d\n", testc, ans1, ans2);
	}
	return 0;
}
