#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, 1, -1};

string a[7];


int n, m;
set<string> se;


int check(int r) {
//	cout << r << endl;
//	for (int i = 0; i < min(n, r + 2); i++) cout << a[i] << endl;
//	cout << endl;

	for (int i = 0; i < m; i++) {
		int eq = 0;
		for (int d = 0; d < 4; d++) {
			int x = r + dx[d];
			int y = (i + dy[d] + m) % m;

			if (x < 0 || x >= n) continue;
			if (a[x][y] == a[r][i]) eq++;
		}		
		if (eq != a[r][i] - '0') return 0;
	}
	return 1;
}

void add() {
	string mi = "";
	for (int i = 0; i < m; i++) {
		string t = "";
		for (int j = 0; j < n; j++) {
			t += a[j].substr(i);
			t += a[j].substr(0, i);
		}
		if (mi == "" || t < mi) mi = t;
	}
	se.insert(mi);
}

void go(int x, int y) {
	if (y == m) {
		if (x > 0 && !check(x - 1)) return;
		if (x == n - 1) {
			if (check(x)) add();
		} else go(x + 1, 0);
		return;
	}
	
	for (int i = 1; i <= 3; i++) {
		a[x][y] = '0' + i;
		go(x, y + 1);
	}
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) a[i].resize(m);

		se.clear();
		go(0, 0);
		cout << "Case #" << tt << ": ";

		cout << se.size() << endl;

	}
	return 0;
}