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

int n, m, ma, kol;
vector<string> a[11];
int st[11111][111];
string s[11];

int f(vector<string> g) {
	int tt = 0;
	for (int i = 0; i < g.size(); i++) {
		int h = 0;
		for (int j = 0; j < g[i].size(); j++) {
			if (!st[h][g[i][j] - 'A']) {
				tt++;
				st[h][g[i][j] - 'A'] = tt;
				h = tt;							
			} else h = st[h][g[i][j] - 'A'];
		}
	}
	for (int i = 0; i <= tt; i++) for (int j = 0; j < 26; j++) st[i][j] = 0;
	return tt + 1;

}

void rec(int x) {
	if (x == m) {
		int bad = 0;
		for (int i = 0; i < n; i++) if (a[i].size() == 0) bad = 1;
		if (bad) return;
		int s = 0;
		for (int i = 0; i < n; i++) s += f(a[i]);
		if (s > ma) {
			ma = s;
			kol = 0;
		}
		if (s == ma) kol ++;
		return;
	}
	for (int i = 0; i < n; i++) {
		a[i].pb(s[x]);
		rec(x + 1);
		a[i].pop_back();
	}
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> m >> n;
		ma = -1, kol = 0;
		for (int i = 0; i < m; i++) cin >> s[i];
		rec(0);
		cout << "Case #" << tt << ": ";
		cout << ma << " " << kol << endl;

	}
	return 0;
}