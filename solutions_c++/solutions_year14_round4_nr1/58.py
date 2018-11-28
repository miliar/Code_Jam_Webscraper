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
 
char used[20000];

int main() {
	int t, n, x, capleft;
	vector <int> cap;

	cin >> t;

	REP(tc,t) {
		cin >> n >> x;
		cap.resize(n);

		REP(i,n) cin >> cap[i];

		sort(cap.rbegin(), cap.rend());
		memset(used, 0, sizeof(used));

		int res = 0;
		REP(i,n) if (!used[i]) {
			++res;
			used[i] = 1;
			capleft = x-cap[i];
			FOR(j,i+1,n) if (!used[j] && capleft >= cap[j]) {
				used[j] = 1;
				break;
			}
		}

		cout << "Case #" << tc+1 << ": " << res << endl;
	}

	return 0;
} 