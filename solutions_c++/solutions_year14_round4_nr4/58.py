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
 
int main() {
	int t, n, m;
	vector <string> s;

	cin >> t;

	REP(tc,t) {
		cin >> m >> n;
		s.resize(m);
		REP(i,m) cin >> s[i];

		int worst = 0, cnt = 0;
		set <string> srv[4];
		REP(msk,1<<(2*m)) {
			REP(i,4) srv[i].clear();			
			REP(i,m) {
				int server = (msk>>(2*i))&3;
				if (server >= n) goto out;
				REP(j,s[i].length()) {
					string pre = s[i].substr(0, j+1);
					srv[server].insert(pre);
				}
			}
			int count = 0;
			REP(i,n) { if (srv[i].size() == 0) goto out; count += srv[i].size(); }
			if (count > worst) { worst = count; cnt = 1; }
			else if (count == worst) ++cnt;
			out:;
		}


		cout << "Case #" << tc+1 << ": " << worst+n << " " << cnt << endl;
	}

	return 0;
} 