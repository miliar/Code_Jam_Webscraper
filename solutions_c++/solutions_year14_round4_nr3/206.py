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
#define N 4444
using namespace std;
typedef pair<int,int> pt;

int n, m, k;
int x[N], y[N], yy[N], xx[N];
int w[N][N], d[N][N];
map<int, int> ma;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> m >> n >> k;
		vector<int> z;
		for (int i = 0; i < k; i++) {
			cin >> y[i] >> x[i] >> yy[i] >> xx[i];
			z.pb(x[i]);
			if (x[i] > 0) z.pb(x[i] - 1);
			if (x[i] < n - 1) z.pb(x[i] + 1);
			z.pb(xx[i]);
			if (xx[i] > 0) z.pb(xx[i] - 1);
			if (xx[i] < n - 1) z.pb(xx[i] + 1);

		}
		sort(z.begin(), z.end());
		ma.clear();
		int e = 0;
		for (int i = 0; i < z.size(); i++) {
			if (i > 0 && z[i - 1] != z[i]) e++;
			ma[z[i]] = e;
		}
		e++;
		e = n;
		for (int i = 0; i < e; i++) for (int j = 0; j < m; j++) w[i][j] = 0;
		for (int i = 0; i < k; i++) {
//			x[i] = ma[x[i]];
//			xx[i] = ma[xx[i]];
			for (int ii = x[i]; ii <= xx[i]; ii++)
				for (int jj = y[i]; jj <= yy[i]; jj++) w[ii][jj] = 1;
		}
//		for (int i = 0; i < e; i++) {	
//			for (int j = 0; j < m; j++) cout << w[i][j];
//			cout << endl;
//		}
		for (int i = 0; i < e; i++) for (int j = 0; j < m; j++) d[i][j] = 1e9;
		deque<pt> Q;
		for (int i = 0; i < e; i++) {
			if (w[i][0]) {
				d[i][0] = 0;
				Q.push_back(mp(i, 0));
			} else {
				d[i][0] = 1;
				Q.push_front(mp(i, 0));
			}
		}
		while (Q.size()) {
			int x = Q.back().F;
			int y = Q.back().S;
			Q.pop_back();
			for (int i = -1; i < 2; i++) for (int j = -1; j < 2; j++) {
				int xx = x + i;
				int yy = y + j;
				if (xx < 0 || xx >= e || yy < 0 || yy >= m) continue;
				int s = d[x][y] + 1 - w[xx][yy];
				if (s < d[xx][yy]) {
					d[xx][yy] = s;
					if (w[xx][yy]) {
						Q.push_back(mp(xx, yy));
					} else {
						Q.push_front(mp(xx, yy));
					}
				}
			}
		}
		int ans = 1e9;
		for (int i = 0; i < e; i++) ans = min(ans, d[i][m - 1]);
		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}