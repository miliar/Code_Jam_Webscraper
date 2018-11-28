#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
#include <map>
#include <deque>
#include <set>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(n);(i)++)
#define REP2(i,s,n) for(int(i)=s;(i)<(n);(i)++)
#define RREP(i,n) for(int(i)=n;(i)>=0;(i)--)

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int a[105][105], n, m;
		cin >> n >> m;
		REP(i,n) REP(j,m) cin >> a[i][j];

		bool is_ok = true;
		REP(i,n) REP(j,m) {
			int c1 = 1, c2 = 1;//, c3 = 1, c4 = 1;
			REP(k,n) if (a[k][j] > a[i][j]) c1 = 0;
			//REP2(k,i+1,n) if (a[k][j] > a[i][j]) c2 = 0;
			REP(k,m) if (a[i][k] > a[i][j]) c2 = 0;
			//REP2(k,j+1,m) if (a[i][k] > a[i][j]) c4 = 0;
			if (c1 + c2 == 0){ // + c3 + c4 == 0) {
				is_ok = false;
			}
		}

		if (is_ok) {
			printf("Case #%d: YES\n", t+1);
		} else {
			printf("Case #%d: NO\n", t+1);
		}
	}

	return 0;
}


