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

int m, n;

void solve(){
	cin >> m >> n;
	string s[10];
	rep(i, m) cin >> s[i];
	
	int ans = -1, answ = 0;
	int pw[10];
	rep(i, 10) pw[i] = i ? pw[i-1] * n : 1;
	
	rep(bit, pw[m]){
		
		set<string> t[n];
		
		rep(i, m){
			int p = bit / pw[i] % n;
			rep(j, s[i].size() + 1) t[p].insert(s[i].substr(0, j));
		}
		
		int tmp = 0;
		rep(i, n) tmp += t[i].size();
		if(tmp > ans) ans = tmp, answ = 0;
		if(tmp == ans) answ++;
	}
	
	cout << ans << " " << answ << endl;
}

int main(){
	int cs; cin >> cs;
	rep(CS, cs){
		cout << "Case #" << CS + 1 << ": ";
		solve();
	}
	return 0;
}