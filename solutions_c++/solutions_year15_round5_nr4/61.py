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

pair<long long, long long> q[N], qq[N], save[N];
int p;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> p;
		for (int i = 0; i < p; i++) cin >> q[i].F;
		long long sum = 0;
		for (int i = 0; i < p; i++) cin >> q[i].S, sum += q[i].S;

		int n = 0;
		while (pw(n) < sum) n++;

		vector<long long> ans;
		for (int i = 0; i < n; i++) {
			sort(q, q + p);
			for (int j = 0; j < p; j++) {
				for (int k = 0; k < p; k++) save[k] = q[k];

				long long x = q[j].F;


				int pp = 0;
				int bad = 0;

				
				if (x > 0) {
					for (int k = 0; k < p; k++) if (q[k].S > 0) {
						long long t = q[k].S;
						int z = lower_bound(q, q + p, mp(q[k].F + x, 0ll)) - q;
						if (q[z].S < t) {
							bad = 1;
							break;
						}
						q[z].S -= t;
						qq[pp++] = q[k];
					}
				} else if (x < 0) {
					for (int k = p - 1; k >= 0; k--) if (q[k].S > 0) {
						long long t = q[k].S;
						int z = lower_bound(q, q + p, mp(q[k].F + x, 0ll)) - q;
						if (q[z].S < t) {
							bad = 1;
							break;
						}
						q[z].S -= t;
						qq[pp++] = q[k];
					}
				} else {
					for (int k = 0; k < p; k++) if (q[k].S % 2) {
						bad = 1;
						break;
					}
					pp = p;
					if (!bad) for (int k = 0; k < p; k++) qq[k] = mp(q[k].F, q[k].S / 2);
				}
				if (bad) {
					for (int k = 0; k < p; k++) q[k] = save[k];
				} else {
					p = pp;
					for (int k = 0; k < p; k++) q[k] = qq[k];
					ans.pb(x);
					break;
				}


					
			}
		}
		cout << "Case #" << tt << ": ";
		for (int i = 0; i < n; i++) {
			cout << ans[i];
			if (i + 1 == n) puts(""); else cout << " "; 
		}

	}
	return 0;
}