#include<bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

void solve(){
	long double c, f, x;
	long double ans = INF;
	long double t = 0;
	
	cin >> c >> f >> x;
	
	for(int build = 0; ; build++){
		
		long double nans = t + x / (build * f + 2);
		
		if(nans > ans + EPS) break;
		ans = nans;
		t += c / (build * f + 2);
	}
	printf("%.9f\n", (double)ans);
}

int main(){
	int cs;
	cin >> cs;
	rep(i, cs){
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}
