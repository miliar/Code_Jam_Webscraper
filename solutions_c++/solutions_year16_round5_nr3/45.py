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

int n, s;
int x[N], y[N], z[N], vx[N], vy[N], vz[N];

double d[N];
int f[N];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> s;
		for (int i = 0; i < n; i++) cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];

		for (int i = 0; i < n; i++) d[i] = 1e18 + 1, f[i] = 0;
		d[0] = 0;
		for(;;) {
			int w = -1;
			for (int i = 0; i < n; i++) if (!f[i] && (w == -1 || d[i] < d[w])) w = i;
			if (w == -1) break;
			f[w] = 1;
			for (int i = 0; i < n; i++) {
				double dist = max(d[w], sqrt((x[w] - x[i]) * (x[w] - x[i]) + (y[w] - y[i]) * (y[w] - y[i]) + (z[w] - z[i]) * (z[w] - z[i])));
				d[i] = min(d[i], dist);
			}

		}
		cout << "Case #" << tt << ": ";
		printf("%.10lf\n", d[1]);

	}
	return 0;
}