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

int n, k;
int ss[N];
vector<pair<int, long long> > v[N];
long long d[N];

int ok() {
//	for (int i = 0; i <= n; i++) for (int j = 0; j < v[i].size(); j++) cout << i << " " << v[i][j].F << " " << v[i][j].S << endl;
	for (int i = 0; i <= n; i++) d[i] = 0;
	for (int i = 0; i <= n; i++) {
		int h = 0;
		for (int j = 0; j <= n; j++) for (int k = 0; k < v[j].size(); k++) {
			int to = v[j][k].F;
			if (d[j] + v[j][k].S < d[to]) {
				if (abs(d[j] + v[j][k].S) < 1e17) {
					d[to] = d[j] + v[j][k].S;
				}					
				h = 1;
			}
		}
		if (!h) return 1;
	}
	return 0;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> k;
		for (int i = 0; i < n - k + 1; i++) cin >> ss[i];

		long long ans = 1e9;
			long long l = -5e10;
			long long r = 5e10;
		
			while (l < r) {
				long long mid = l + (r - l) / 2;
				for (int i = 0; i <= n; i++) v[i].clear();
		
				for (int i = 0; i < n - k + 1; i++) {
					v[i + k].pb(mp(i, -ss[i]));
					v[i].pb(mp(i + k, ss[i])); 
				}
				for (int i = 0; i < n; i++) {
//					v[i + 1].pb(mp(i, -mid));
					v[i].pb(mp(i + 1, mid));
				}
				if (ok()) r = mid; else l = mid + 1;
			}
			long long mi = l;
//			cerr << l << endl;

			l = 0;
			r = 5e10;
		
			while (l < r) {
				long long mid = (l + r) / 2;
				for (int i = 0; i <= n; i++) v[i].clear();
		
				for (int i = 0; i < n - k + 1; i++) {
					v[i + k].pb(mp(i, -ss[i]));
					v[i].pb(mp(i + k, ss[i])); 
				}
				for (int i = 0; i < n; i++) {
					v[i + 1].pb(mp(i, -mi + mid));
					v[i].pb(mp(i + 1, mi));
				}
				if (ok()) r = mid; else l = mid + 1;
			}
			
			ans = l;

		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}