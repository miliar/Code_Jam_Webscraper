#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
string s[100];
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};
int H,W;
bool is(int x,int y){
	return 0<=x&&x<H&&0<=y&&y<W;
}
bool ok(int x,int y,int d){
	x+=dx[d],y+=dy[d];
	while(is(x,y)){
		if(s[x][y]!='.') return true;
		x+=dx[d],y+=dy[d];
	}
	return false;
}
void solve(){
	cin>>H>>W;
	rep(i,H) cin>>s[i];
	int ans=0;
	rep(i,H) rep(j,W){
		if(s[i][j]=='.') continue;
		int d=0;
		if(s[i][j]=='v') d=0;
		if(s[i][j]=='>') d=1;
		if(s[i][j]=='^') d=2;
		if(s[i][j]=='<') d=3;
		if(ok(i,j,d)) continue;
		bool ook=0;
		rep(k,4) if(ok(i,j,k)) ook=1;
		if(!ook){
			puts("IMPOSSIBLE");
			return;
		}
		ans++;
	}
	cout<<ans<<endl;
}
int main(){
	int T;
	cin>>T;
	rep1(tt,T){
		printf("Case #%d: ",tt);
		solve();
	}
}
