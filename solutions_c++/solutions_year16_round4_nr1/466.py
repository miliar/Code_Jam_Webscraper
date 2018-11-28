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

string build(char c, int h) {
	if(h==0) {
		if(c == 'P') return "P";
		if(c == 'R') return "R";
		return "S";
	}
	vector<string> v;
	if(c == 'P') v.pb("P");
	else if(c == 'R') v.pb("R");
	else v.pb("S");
	
	for(int i=0; i<h; i++) {
		if(c == 'P') v.pb(build('R', i));
		else if(c == 'R') v.pb(build('S', i));
		else v.pb(build('P', i));
	}
	string res = v[0];
	for(int i=1; i<v.size(); i++) {
		if(res < v[i]) res += v[i];
		else res = v[i] + res;
	}
	return res;
}

void solve() {
	int n,R,P,S;
	cin>>n>>R>>P>>S;
	vector<string> res;
	string s1 = build('P', n);
	//cout<<"P "<<s1<<"\n";
	int P1 = count(s1.begin(), s1.end(), 'P');
	int R1 = count(s1.begin(), s1.end(), 'R');
	int S1 = count(s1.begin(), s1.end(), 'S');
	if(P1 == P && R1 == R && S1 == S) res.pb(s1);

	s1 = build('R', n);
	//cout<<"R "<<s1<<"\n";
	P1 = count(s1.begin(), s1.end(), 'P');
	R1 = count(s1.begin(), s1.end(), 'R');
	S1 = count(s1.begin(), s1.end(), 'S');
	if(P1 == P && R1 == R && S1 == S) res.pb(s1);

	s1 = build('S', n);
	//cout<<"S "<<s1<<"\n";
	P1 = count(s1.begin(), s1.end(), 'P');
	R1 = count(s1.begin(), s1.end(), 'R');
	S1 = count(s1.begin(), s1.end(), 'S');
	if(P1 == P && R1 == R && S1 == S) res.pb(s1);
	
	if(res.size()==0) cout<<"IMPOSSIBLE\n";
	else {
		sort(res.begin(), res.end());
		cout<<res[0]<<"\n";
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}