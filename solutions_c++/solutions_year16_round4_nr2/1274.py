#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb(x) push_back(x)
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0); 
//#define NDEBUG 1
#define fst first
#define snd second
#define sz(v) ((int)v.size())
typedef vector<int> vi;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int tc;
int n, k;
ld p[220];
vector<ld> v;

ld dp[220][220];

ld go(int i, int y){
	if (i == k) {
		if (y == 0) return 1.0;
		else return 0.0;
	}
	if (dp[i][y] > -1) return dp[i][y];
	
	ld ans = 0;
	if (y) ans += v[i] * go(i+1, y-1);
	ans += (1-v[i]) * go(i+1, y);
//	cerr << "dp[" << i << "][" << y << "]: " << ans << endl;
	return dp[i][y] = ans;
}


int main(){
	fast_io();
	cin >> tc;
	REP(zz,1,tc+1){
		cin >> n >> k;
		REP(i,0,n) cin >> p[i];
		sort(p,p+n);
		
		ld best = 0;
		vector<int> w;
		REP(i,0,n-k) w.pb(0);
		REP(i,0,k) w.pb(1);
		do {
			v.clear();
			REP(i,0,n) if (w[i]) v.pb(p[i]);
			sort(all(v));
			REP(i,0,sz(v)) REP(j,0,sz(v)) dp[i][j] = -5;
			best = max(best, go(0,k/2));
		} while (next_permutation(all(w)));

		cout << "Case #" << zz << ": " << setprecision(6) << fixed << best << endl;
	}
	return 0;
}

