#include <bits/stdc++.h>
#define FOR(i,a,b) for(LL i=(a);i<(b);i++)
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
typedef int ut;
typedef vector<ut> VI;
typedef pair<ut,ut> pr;
typedef vector<pr> Vpr;
typedef pair<ut,pr> ppr;
typedef vector<ppr> Vppr;
typedef priority_queue<ppr,Vppr,greater<ppr> > PQ;
typedef vector<ppr> Vppr;
const int SIZE=100+1e+5;
const int INF=1<<30;
char maps[101][101];
int R,C;
bool ask(int y,int x,char c){
	if(c=='^') y-=1;
	else if(c=='v') y+=1;
	else if(c=='>') x+=1;
	else if(c=='<') x-=1;
	if(x<0 || y<0 || y>=R || x>=C) return false;
	if(maps[y][x]!='.') return true;
	return ask(y,x,c);
}
bool solve(int t){
	cin >> R >> C;
	string s;
	REP(i,R){
		cin >> s;
		REP(j,C)
			maps[i][j]=s[j];
	}
	int ans=0;
	REP(i,R)
		REP(j,C){
			if(maps[i][j]!='.'){
				if(ask(i,j,maps[i][j]))
					continue;
				ans++;
				if(ask(i,j,'^')||ask(i,j,'<')||ask(i,j,'v')||ask(i,j,'>'))
					continue;
				return false;
			}
	
	}
	
	printf("Case #%d: %d\n",t,ans);
	return true;
}
int main(){
	int T;
	cin >> T;
	FOR(i,1,T+1){
		if(!solve(i))
			printf("Case #%d: IMPOSSIBLE\n",i);
	}
	return 0;
}