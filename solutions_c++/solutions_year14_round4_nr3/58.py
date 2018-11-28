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
 
int o[1000][4];

int d[1024][1024];
int src, dst;

int dist(int l1, int r1, int l2, int r2) {
	if (r2<l1) return l1-r2-1;
	if (r1<l2) return l2-r1-1;
	return 0;
}

int sp[1024];
char ok[1024];

int main() {
	int t, w, h, b;

	cin >> t;

	REP(tc,t) {
		cin >> w >> h >> b;
		src = b; dst = b+1;
		REP(i,b) {
			REP(j,4) cin >> o[i][j];
			d[i][src] = d[src][i] = o[i][0];
			d[i][dst] = d[dst][i] = w-1-o[i][2];
		}

		d[src][dst] = d[dst][src] = w;

		REP(i,b) FOR(j,i+1,b) {
			int D1 = dist(o[i][0], o[i][2], o[j][0], o[j][2]);
			int D2 = dist(o[i][1], o[i][3], o[j][1], o[j][3]);
			//int D = D1 > 0 && D2 > 0 ? D1+D2-1 : D1+D2;
			int D = max(D1,D2);
			d[i][j] = d[j][i] = D;
		}
		REP(i,b+2) d[i][i] = 0;

		REP(i,b+2) { sp[i] = 1<<30; ok[i] = 0; }
		sp[src] = 0; ok[src] = 1;
		REP(i,b+2) {
			sp[i] = min(sp[i], sp[src]+d[src][i]);
		}

		while (!ok[dst]) {
			int next = -1, nextdst = 1<<30;
			REP(i,b+2) if (!ok[i] && sp[i] < nextdst) { nextdst = sp[i]; next = i; }
			ok[next] = 1;
			REP(i,b+2) sp[i] = min(sp[i], sp[next]+d[next][i]);
		}

		cout << "Case #" << tc+1 << ": " << sp[dst] << endl;
	}

	return 0;
} 