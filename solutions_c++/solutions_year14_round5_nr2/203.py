#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <complex>
 
using namespace std;
 
 
#define REP(a,b) for (int a=0; a<(int)(b); ++a)
#define FOR(a,b,c) for (int a=(b); a<(int)(c); ++a)
 
int m[100][2024];
int h[100], g[100];
int p, q, n;

int go(int pos, int saved) {
	if (pos == n) return 0;
	if (m[pos][saved] < 0) {
		int tkill = (h[pos]+q-1)/q;
		m[pos][saved] = go(pos+1, saved+tkill);
		int nshots = (h[pos]-(tkill-1)*q + p - 1)/p;
		if (tkill-1+saved >= nshots) {
			m[pos][saved] = max(m[pos][saved], g[pos]+go(pos+1, saved+tkill-1-nshots));
		}
	}

	return m[pos][saved];
}

int main() {
	int t;

	cin >> t;

	REP(tc,t) {
		cin >> p >> q >> n;
		REP(i,n) cin >> h[i] >> g[i];

		memset(m, -1, sizeof(m));

		cout << "Case #" << tc+1 << ": " << go(0,1) << endl;
	}

	return 0;
} 