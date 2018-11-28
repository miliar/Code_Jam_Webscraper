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
 
char used[2000];

int main() {
	int t, n, res, L, R, pos;
	vector <int> a, b;

	cin >> t;

	REP(tc,t) {
		cin >> n;
		a.resize(n); b.resize(n);

		REP(i,n) { cin >> a[i]; b[i] = a[i]; }
		sort(b.begin(), b.end());

		memset(used, 0, sizeof(used));

		res = 0;
		REP(i,n) {
			pos = 0; L = R = 0;
			while (pos < n && a[pos] != b[i]) { if (!used[pos]) ++L; ++pos; }
			used[pos] = 1; ++pos;
			while (pos < n) { if (!used[pos]) ++R; ++pos; }
			res += min(L,R);
		}

		cout << "Case #" << tc+1 << ": " << res << endl;
	}

	return 0;
} 