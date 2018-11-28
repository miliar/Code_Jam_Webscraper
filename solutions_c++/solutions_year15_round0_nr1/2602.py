#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,b) FOR(i,0,b)
#define F first
#define S second
#define X first
#define Y second
#define PB push_back 
#define BE(c) c.begin(),c.end()
using namespace std;
typedef long long LL;
typedef complex<int> cld;
typedef LL ut;
typedef vector<ut> VI;
typedef pair<ut,ut> pr;
typedef vector<pr> Vpr;
typedef pair<ut,pr> ppr;
typedef vector<ppr> Vppr;
typedef pair<pr,pr> ppppr;
typedef pair<ut,ppppr> pppppr;
typedef priority_queue<ppr,Vppr> PQ;
typedef vector<ppr> Vppr;
const int SIZE=1+1e+5;
const int INF=1<<30;
const LL p=7+1e+9;

int solve(){
	int sm;
	cin >> sm;
	string s;
	cin >> s;
	int sum=0;
	int need=0;
	REP(i,sm+1){
		if(s[i]=='0')continue;
		if(sum<i){
			need+=i-sum;
			sum=i;
		}
		sum+=s[i]-'0';
	}
	return need;
}
int main(){
	int N;
	cin >> N;
	REP(i,N)
	cout << "Case #"<< i+1 << ": " << solve() << endl;
	return 0;
}