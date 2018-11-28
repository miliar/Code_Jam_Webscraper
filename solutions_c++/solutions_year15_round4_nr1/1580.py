#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(I,C) for(__typeof(C.begin()) I = (C).begin(); I != (C).end(); I++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair

#define MAX 128

int R, C;
string orig[MAX], tab[MAX];
int mapdir[10000];

char ops[] = {'v', '^', '<', '>'};
int dx[] = {0, 1, -1, 0, 0};
int dy[] = {0, 0, 0, -1, 1};


void debug_tab(int ok) {
	if (ok >= -1) return;
	cout << "OK = " << ok << endl;
	FOR(r, R) {
		cout << tab[r] << endl;
	}
	cout << endl;
}


int newdir(int r, int c, int dir) {
	if (tab[r][c] == '.') {
		return dir;
	}
	return mapdir[ tab[r][c] ];
}

bool move_out(int r, int c, int dir) {
	if (r < 0 || r >= R || c < 0 || c >= C) {
		return true;
	}

	int xdir = newdir(r,c,dir);
	// '.'
	if (xdir == 0) {
		return false;
	} 
	// achou seta
	if (dir != 0 && tab[r][c] != '.') {
		return false;
	}

	return move_out( r + dx[xdir] , c + dy[xdir], xdir );
}

bool run_outside(int r, int c) {
	return move_out(r, c, 0);
}

int change_bad() {

	int ans = 0;
	FOR(r, R) {
		FOR(c, C) {
			if (!run_outside(r, c)) continue;
			FOR(d, 4) {
				char old = tab[r][c];
				tab[r][c] = ops[d];
				if (!run_outside(r, c)) {
					ans++; 
					break;
				}
				tab[r][c] = old;
			}
			if (run_outside(r, c)) return R * C + 1; 
		}
	}

	return ans;
}


void solve() {
	mapdir[ops[0]] = 1;
	mapdir[ops[1]] = 2; 
	mapdir[ops[2]] = 3;
	mapdir[ops[3]] = 4;

	cin >> R >> C;
	FOR(i, R) {
		cin >> orig[i];
		tab[i] = orig[i];
	}

	debug_tab(-1);

	int ans = change_bad();
	if (ans > R * C) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout << ans << endl;
}

int main() {
  int num_testes;
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
