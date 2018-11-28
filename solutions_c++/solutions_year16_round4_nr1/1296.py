#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,b) FOR(i,0,b)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define TT second.second
#define SS second.first
#define FF first
using namespace std;
typedef long long LL;
typedef double ut;
typedef vector<ut> VI;
typedef pair<ut,ut> pr;
typedef pair<ut,pr> ppr;
typedef vector<pr> Vpr;
typedef priority_queue<pr,Vpr,greater<pr> > PQ;
const int INF=1<<30;
const int BITSIZE=1<<12;
const int SIZE=10+2*1e4;
string jang[]={"R","P","S"};
ppr DP[BITSIZE+5][BITSIZE+5];
bool checked[BITSIZE+5][BITSIZE+5];
ppr pprs(int a,int b,int c){
	return ppr(a,pr(b,c));
}
ppr sum(ppr a,ppr b){
	return pprs(a.FF+b.FF,a.SS+b.SS,a.TT+b.TT);
}
ppr solve(int n,int h){
	//cout << n << " " << h <<" " << DP[n][h].FF <<" " << DP[n][h].SS <<" " << DP[n][h].TT << endl;
	if(checked[n][h]) return DP[n][h];
	checked[n][h]=true;
	if(n==0) return DP[n][h]=pprs(h==0,h==1,h==2);
	return DP[n][h]=sum(solve(n-1,h),solve(n-1,(h+2)%3));
}
string output(int n,int h){
	string a,b;
	if(n==0){
		return (string)jang[h];
	}
	a=output(n-1,h);
	b=output(n-1,(h+2)%3);
	return min(a+b,b+a);
}
int main(){
	int T;
	cin.tie(0);
	cin >> T;
	int N,R,P,S;
	FOR(i,1,T+1){
		cout << "Case #" << i <<": ";
		cin >> N >> R >> P >> S;
		ppr input=pprs(R,P,S);
		//cout << N <<" " <<x.FF <<" " << x.SS <<" " << x.TT << endl;
		bool ans=false;
		REP(j,3){
			if(solve(N,j)==input){
				cout << output(N,j) << endl;
				ans=true;
				break;
			}
		}
		if(!ans) cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}