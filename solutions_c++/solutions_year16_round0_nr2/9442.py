#include <bits/stdc++.h>

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define FOR(i,n) REP(i,0,(int)n-1)
#define mp make_pair
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define VI vector<int>
#define fi first
#define se second
#define pss pair<short int, short int>

/*map<string,int> M;

char flip(char c) {
	if(c=='+') return '-';
	return '+';
}

int  brut(string s) {
	if(M.find(s) != M.end()) return M[s];
	int mini = 4042;
	for(int i=1; i<=s.size(); i++) {
		string s2;
		REP(j,0,i-1) s2+=flip(s[i-1-j]);
		REP(j,i,s.size()-1) s2+=s[j];
		int mini = min(mini,brut(s2));
	}
	M[s] = mini + 1;
	return mini + 1;
}*/

void solve() {
	string s;
	cin>>s;
	char last = s[0];
	int res = 0;
	FOR(i,s.size()) {
		if(s[i]!=last) res++;
		last = s[i];
	}
	if(s[s.size()-1] == '-') res++;
	cout<<res<<"\n";
}

int main() {
	ios_base::sync_with_stdio(0);
	/*REP(i,1,100) {
		string temp = "";
		FOR(j,i) temp += "1";
		M[temp] = 0;
	}
	REP(i,1,(1<<10)) {
		string s = trans(i);
	}*/
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}