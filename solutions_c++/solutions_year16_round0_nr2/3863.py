#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,b) FOR(i,0,b)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define PS second
#define PF first
using namespace std;
typedef long long LL;
typedef LL ut;
typedef pair<ut,ut> pr;
typedef vector<ut> VI;
typedef vector<pr> Vpr;
typedef priority_queue<pr,Vpr,greater<pr> > PQ;
const int p=7+1e9;
const int SIZE=1+2*1e+5;
const int INFi=1<<30;
const LL INF=1LL<<55;

int main(){
	
	int T;
	cin >> T;
	REP(j,T){
		string s;
		cin >> s;
		s+='+';
		int ans=0;
		REP(i,s.size()-1){
			ans+=s[i]!=s[i+1];
		}
		cout << "Case #"<<j+1 <<": " << ans << endl;
	}

	return 0;
}