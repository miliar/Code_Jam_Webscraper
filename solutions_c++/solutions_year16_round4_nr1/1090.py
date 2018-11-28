#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
const int    INF = 100000000;
const double EPS = 1e-10;
const int    MOD = 1000000007;
using namespace std;
typedef pair<int,int> P;

int n, x[3], m;
int y[3];

string output(string s){
	for(int i = 1; i < m; i *= 2){
		for(int j = 0;; j += 2*i){
			int k = j+i;
			if(k >= m) break;
			string s1 = s.substr(j,i), s2 = s.substr(k,i);
			if(s1 > s2){
				rep(u,i) s[j+u] = s2[u];
				rep(u,i) s[k+u] = s1[u];
			}
		}
	}
	return s;
}

string out(int z){
	if(z == 0) return "R";
	if(z == 1) return "P";
	if(z == 2) return "S";
	return "";
}

string dfs(int t, int d){
	string v;
	if(d == n){
		y[t]--;
		return out(t);
	}
	if(t == 0){
		v =dfs(0,d+1)+dfs(2,d+1);
	}
	if(t == 1){
		v=dfs(1,d+1)+dfs(0,d+1);
	}
	if(t == 2){
		v=dfs(1,d+1)+dfs(2,d+1);
	}
	return v;
}

void solve(){
	cin >> n;
	rep(i,3) cin >> x[i];
	m = 1;
	rep(i,n) m *= 2;
	rep(i,3){
		rep(j,3) y[j] = x[j];
		string ans = dfs(i,0);
		bool ok = true;
		rep(j,3) if(y[j] != 0) ok = false;
		if(ok){
			cout << output(ans) << endl;
			return;
		}
	}
	cout << "IMPOSSIBLE" << endl;
}

int main(){
	int T;
	cin >> T;
	rep(i,T){
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}