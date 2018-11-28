#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cstring>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPR(i,a,b) for (int i = a; i <= b; i++)

const int N = 15;
int v[N][N], r, c;
bool seen[N][N];

bool ok(int x, int y) {
	return x >= 0 && y >= 0 && x < r && y < c;
}
int get(int x, int y) {
	return ok(x,y) ? v[x][y] : 0;
}
int cnt(int x, int y) {
	int ans = 0;
	REPR(i,-1,1) REPR(j,-1,1) ans += get(x+i,y+j);
	return ans;
}

void dfs(int x, int y) {
	if (!ok(x,y)) return;
	if (seen[x][y]) return;
//	cout << "!" << x << " " << y << endl;
	seen[x][y] = true;
	if (cnt(x,y) == 0) {
		//expand!
		REPR(i,-1,1) REPR(j,-1,1) if (i || j) dfs(x+i,y+j);
	}
}

int t, m;

int main() {
	cin >> t;
	REP(qqq,t) {
		cin >> r >> c >> m;
		assert(m < r*c);
		cout << "Case #" << (qqq+1) << ": " << endl;
		if (r*c == m+1) {
			//just leave corner empty
			cout << "c";
			REP(j,r) {
				REP(k,c-(j==0)) cout << "*";
				cout << endl;
			}
		} else {
			bool done = false;
			REP(i,1<<(r*c)) if (__builtin_popcount(i) == m) {
				//good configuration?
				//set of 0s must be connected
				//and all other non-mines adjacent to a 0
//				cout << "          " << i << endl;
				REP(j,r) REP(k,c) v[j][k] = (i & (1<<(j*c+k))) ? 1 : 0;
				bool flag = false;
				memset(seen,0,sizeof(seen));
	//			cout << "!" << endl;
				pair<int,int> click;
				REP(j,r) REP(k,c) if (!flag && cnt(j,k)==0) {
					//try here!
//					cout << j << " " << k << endl;
					dfs(j,k);
					flag = true;
					click=make_pair(j,k);
				}
	//			cout << "!" << endl;
				bool ok = true;
				REP(j,r) REP(k,c) if (!v[j][k]&&!seen[j][k]) ok = false;
				if (ok) {
//					cout << i << " " << ok << endl;
					REP(j,r) {
						REP(k,c) {
							if (j==click.first&&k==click.second)
							cout << "c";
							else
							cout << (v[j][k]?"*":".");
						}
						cout << endl;
					}
					i = 1<<(r*c)+1; //kill loop
					done = true;
				}
			}
			if (!done)
				cout << "Impossible" << endl;
		}
	}
}
