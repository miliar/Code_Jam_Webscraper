#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define FOR(prom, a, b) for(int prom = (a); prom < (b); prom++)
#define FORD(prom, a, b) for(int prom = (a); prom > (b); prom--)
#define FORDE(prom, a, b) for(int prom = (a); prom >= (b); prom--)

#define DRI(a) int a; scanf("%d ", &a);
#define DRII(a, b) int a, b; scanf("%d %d ", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d ", &a, &b, &c);
#define DRIIII(a, b, c, d) int a, b, c, d; scanf("%d %d %d %d ", &a, &b, &c, &d);
#define RI(a) scanf("%d ", &a);
#define RII(a, b) scanf("%d %d ", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d ", &a, &b, &c);
#define RIIII(a, b, c, d) scanf("%d %d %d %d ", &a, &b, &c, &d);

#define PB push_back
#define MP make_pair

#define ll long long
#define ull unsigned long long

#define MM(co, cim) memset((co), (cim), sizeof((co)))

#define DEB(x) cerr << ">>> " << #x << " : " << x << endl;

string names[13];
int ser[13];
int M,N;
int maxdiff, cntdiff;
vector<string> sernames[7];

void calc() {
	FOR(i,0,N) sernames[i].clear();
	FOR(i,0,M) sernames[ser[i]].PB(names[i]);
	FOR(s,0,N) if(sernames[s].size() == 0) return;
	int c = 0;
	FOR(s,0,N) {
		FOR(n,0,sernames[s].size()) {
			if(n == 0) c += sernames[s][n].length()+1;
			else {
				bool same = true;
				FOR(i,0,min(sernames[s][n-1].length(),sernames[s][n].length())) {
					if(sernames[s][n-1][i] != sernames[s][n][i]) same = false;
					if(!same) c++;
				}
				if(sernames[s][n-1].length() < sernames[s][n].length()) c += sernames[s][n].length() - sernames[s][n-1].length();
			}
		}
	}
	if(c > maxdiff) {
		maxdiff = c;
		cntdiff = 1;
	} else if(c == maxdiff) cntdiff++;
	cntdiff %= 1000000007;
}

void rec(int p) {
	if(p == M) {
		calc();
		return;
	}
	FOR(i,0,N) {
		ser[p] = i;
		rec(p+1);
	}
}

int main ()
{
  DRI(T);
  FOR(t,1,T+1) {
  	RII(M,N);
  	FOR(m,0,M) cin >> names[m];
  	sort(names,names+M);
  	maxdiff = -1;
  	cntdiff = 0;
  	rec(0);
  	printf("Case #%d: %d %d\n", t, maxdiff, cntdiff);
  }
  return 0;
}
