#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,b) FOR(i,0,b)
#define F first
#define S second
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

bool solve(){
	LL L,X;
	cin >> L;
	cin >> X;

	if(X>20)
		X=X%4+20;
	string s;
	cin >> s;
	string use="";
	REP(i,X) use+=s;
	int now=0;
	char nowchar='1';
	bool isplus=true;
	REP(i,use.size()){
		if(nowchar=='1'){
			nowchar=use[i];
		}
		else if(nowchar==use[i]){
			nowchar='1';
			isplus^=1;
		}
		else if(nowchar!='j' && use[i]!='j'){
			if(nowchar=='i') isplus^=1;
			nowchar='j';
		}
		else if(nowchar!='k' && use[i]!='k'){
			if(nowchar=='j') isplus^=1;
			nowchar='k';
		}
		else if(nowchar!='i' && use[i]!='i'){
			if(nowchar=='k') isplus^=1;
			nowchar='i';
		}
		if(isplus)
			if((now==0 && nowchar=='i')||(now==1&&nowchar=='j')||(now==2&&nowchar=='k')){
					now++;
					nowchar='1';
			}
	}
	return nowchar=='1' && isplus && now==3;
}
int main(){
	int N;
	cin >> N;
	REP(i,N)
	cout << "Case #"<< i+1 << ": " << (solve()?"YES":"NO") << endl;
	return 0;
}