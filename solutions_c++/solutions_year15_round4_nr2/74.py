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

int n;
long double V, X, r[222], c[222];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> V >> X;
		for (int i = 0; i < n; i++) cin >> r[i] >> c[i];

		for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (c[i] > c[j]) {
			swap(c[i], c[j]);
			swap(r[i], r[j]);
		}

		long double ll = 0;
		long double rr = 3e6;

		for (int it = 0; it < 150; it++) {
			long double mid = (ll + rr) / 2;

			long double curv = 0;
			long double curt = 0;

			for (int i = 0; i < n; i++) {
				long double av = min(V - curv, mid * r[i]);
				curt = (curt * curv + av * c[i]) / (curv + av);
				curv += av;
			}

			if (curv < V - 1e-10) {
				ll = mid;
				continue;
			}
			long double t1 = curt;

			curv = 0;
			curt = 0;

			for (int i = n - 1; i >= 0; i--) {
				long double av = min(V - curv, mid * r[i]);
				curt = (curt * curv + av * c[i]) / (curv + av);
				curv += av;
			}

			long double t2 = curt;

			if (t1 < X + 1e-10 && X < t2 + 1e-10) rr = mid; else ll = mid;
		}

		cout << "Case #" << tt << ": ";

		if (ll > 2e6) puts("IMPOSSIBLE"); else
		printf("%.10lf\n", (double) (ll + rr) / 2);

	}
	return 0;



}