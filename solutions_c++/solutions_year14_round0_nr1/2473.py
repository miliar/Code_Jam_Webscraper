#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

#define clr(a, x)  memset(a, x, sizeof(a))
#define REP(i, n)  for(int i = 0; i < (n); i++)
#define DEBUG

typedef long long LL;

int a[4][4], b[4][4];
void solve() {
	int T, r1, r2;
	cin >> T;
	REP(Case, T) {
		cin >> r1;
		REP(i, 4) REP(j, 4)  cin >> a[i][j];
		cin >> r2;
		REP(i, 4) REP(j, 4)  cin >> b[i][j];
		int cnt = 0, ret = -1;
		REP(i, 4) {
			int x = a[r1-1][i];
			REP(j, 4)  if(b[r2-1][j]==x) {
				++cnt;
				ret = x;
			}
		}
		cout << "Case #" << Case+1 << ": ";
		if(cnt == 0)  cout << "Volunteer cheated!" << '\n';
		else if(cnt > 1)  cout << "Bad magician!" << '\n';
		else  cout << ret << '\n';
	}
}

int main() {
#ifdef DEBUG
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	solve();
#ifdef DEBUG
	fclose(stdin);
	fclose(stdout);
#endif
	return  0;
}













