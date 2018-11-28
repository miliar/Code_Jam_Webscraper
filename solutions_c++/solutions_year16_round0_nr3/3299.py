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
const int INFi=1<<30;
const LL INF=1LL<<55;
const int SIZE=4*1e+7;
int main(){
	int T,N,J;
	cin >> T >> N >> J;
	int times=(N-4)/2;
	cout << "Case #1:" << endl;
	REP(i,J){
		cout <<"11" ;
		REP(j,times) cout << (((i&(1<<j))!=0) ? "11" : "00");
		cout << "11 ";
		FOR(j,2,11){
			cout << j+1 << ((j==10)? "":" ");
		}
		cout << endl;
	}

	return 0;
}