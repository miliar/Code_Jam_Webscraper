#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int TESTS, CASE;

const int MAXN = 505;

int n, m, b, x[MAXN][2], y[MAXN][2];

int a[MAXN][MAXN], in[MAXN][MAXN];

int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

bool dfs(int p, int q, int d) {
	in[p][q] = true;
	
	if(q==m-1) {
		return true;
	}
	
	for(int k = -1; k <= 1; k++) {
		int nd = (4+d+k)%4;
		int np = p+dir[nd][0];
		int nq = q+dir[nd][1];
		if(np>=0 && np<n && nq>=0 && nq<m && !a[np][nq] && !in[np][nq]) {
			if(dfs(np,nq,nd)) {
				return true;
			}
		}
	}
	return false;
}

void solve() {
	cout << "Case #" << CASE << ": ";
	
	memset(a,0,sizeof(a));
	memset(in,0,sizeof(in));
	for(int i = 0; i < b; i++) {
		for(int p = x[i][0]; p <= x[i][1]; p++) {
			for(int q = y[i][0]; q <= y[i][1]; q++) {
				a[p][q] = 1;
			}
		}
	}
	
	int ans = 0;
	for(int i = 0; i < n; i++) {
		if(!a[i][0]) {
			ans += dfs(i,0,0);
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n >> m >> b;
		for(int i = 0; i < b; i++) {
			for(int j = 0; j < 2; j++) {
				cin >> x[i][j] >> y[i][j];
			}
		}
		solve();
	}
}
