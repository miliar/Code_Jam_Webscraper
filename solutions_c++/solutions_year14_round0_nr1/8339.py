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
	int a[4][4], b[4][4], x, y;
	set<int> cand;
	int ans = -1;
	
	cin >> x;
	rep(i, 4) rep(j, 4){
		cin >> a[i][j];
		if(x == i + 1) cand.insert(a[i][j]);
	}
	
	cin >> y;
	rep(i, 4) rep(j, 4){
		cin >> b[i][j];
		if(y == i + 1 && cand.count(b[i][j])){
			
			if(ans == -1) ans = b[i][j];
			else ans = -2;
		}
	}
	
	if(ans >= 0) cout << ans << endl;
	else if(ans == -1) cout << "Volunteer cheated!" << endl;
	else cout << "Bad magician!" << endl;
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
