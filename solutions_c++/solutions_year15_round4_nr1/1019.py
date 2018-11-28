#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#define make_pair(a, b) MP(a, b)
#define push_back(a) PB(a)

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 0x3f3f3f3f;
const int LEN = 111;
char Map[LEN][LEN];
int cnt, is, n, m;
int xx[] = {0, 0, 1,-1};
int yy[] = {1,-1, 0, 0};

bool go(int op, int a, int b) {
	while(a >= 0 && a < n && b >= 0 && b < m) {
		a += xx[op]; b += yy[op];
		if(!(a >= 0 && a < n && b >= 0 && b < m))return false;
		if(Map[a][b] != '.') return true;
	}
	return false;
}

bool J(int x, int y) {
	for(int i=0; i<4; i++) {
		if(go(i, x, y)) return true;
	}
	return false;
}

void solve(int a, int b) {
	if(Map[a][b] == '>' && go(0, a, b)) return ;
	if(Map[a][b] == '<' && go(1, a, b)) return ;
	if(Map[a][b] == 'v' && go(2, a, b)) return ;
	if(Map[a][b] == '^' && go(3, a, b)) return ;
	if(J(a, b)) cnt ++;
	else is = 1;
}

void debug() {
	for(int i=0; i<n; i++)
		cout << Map[i] << endl;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("outA.txt", "w", stdout);

	int T, kase = 1;
	cin >> T;
	while(T--) {
		cin >> n >> m;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				cin >> Map[i][j];
			}
		}
	//	debug();
		cnt = is = 0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(Map[i][j] != '.') solve(i, j);
			}
		}
		cout << "Case #" << kase ++ << ": ";
		if(is) cout << "IMPOSSIBLE" << endl;
		else cout << cnt << endl;
	}
	return 0;
}
