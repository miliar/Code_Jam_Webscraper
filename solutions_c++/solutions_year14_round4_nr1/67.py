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

int n, x, s[10000];

void solve(){
	cin >> n >> x;
	rep(i, n) cin >> s[i];
	sort(s, s + n);
	
	int ans = 0;
	
	for(int i = 0, j = n - 1; i < n; i++) if(s[i] < inf){
		while(j >= 0 && s[i] + s[j] > x) j--;
		if(j >= 0 && s[i] + s[j] <= x) s[j--] = inf;
		s[i] = inf;
		ans++;
	}
	cout << ans << endl;
}

int main(){
	int cs; cin >> cs;
	rep(CS, cs){
		cout << "Case #" << CS + 1 << ": ";
		solve();
	}
	return 0;
}