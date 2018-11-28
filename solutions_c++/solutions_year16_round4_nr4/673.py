#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#ifndef ONLINE_JUDGE
	#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#else
	#define DEBUG(x) do {} while(0);
#endif

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
typedef long long ll;
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

int n,m;
int T;
char mtx[60][60];
char mtx2[50][50];
int perm[10];
int assigned[10];
bool good;
void assign(int i) {
	if(i == n)
		return;
	bool found = false;
	for(int j = 0; j < n; j++) {
		//printf("%s\n", mtx2[perm[i]]);
		if(mtx2[perm[i]][j]=='1' && !assigned[j]) {
			found = true;
			assigned[j] = true;
			assign(i+1);
			assigned[j] = false;
		}
	}
	if(!found)
		good = false;
}
bool ok() {
	REP(i, n) perm[i] = i;
	good = true;
	do {
		assign(0);
		if(!good)
			break;
	} while(next_permutation(perm, perm+n));
	return good;
}
void solve() {
	scanf("%d", &n);
	REP(i, n) scanf("%s", mtx[i]);
	int ans = 1000000;
	for(int M = 0; M < (1<<(n*n)); M++) {
		int price = 0;
		for(int k = 0; k < n*n; k++) {
			mtx2[k/n][k%n] = max(mtx[k/n][k%n], (char)('0'+((M&(1<<k))>0)));
		//	printf("%s\n", mtx2[k/n]);
			if(mtx2[k/n][k%n] != mtx[k/n][k%n])
				price++;
		}
		if(ok()) {
			ans = min(ans, price);
		}
	}

	printf("%d", ans);
}

int main() {
	scanf("%d", &T);
	REP(testc, T) {
		printf("Case #%d: ", testc+1);
		solve();
		printf("\n");
	}
	return 0;
}
