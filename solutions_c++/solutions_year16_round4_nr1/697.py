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
template<class S,class T> ostream& operator<<(ostream& o,const pair<S,T> &p){return o<<"("<<p.fs<<","<<p.sc<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T> &vc){o<<"sz = "<<vc.size()<<endl<<"[";for(const T& v:vc) o<<v<<",";o<<"]";return o;}
int N,R,P,S;
string s="PRS";
string memo[14][3];
string calc(int x,int w){
	if(!memo[x][w].empty()) return memo[x][w];
	if(x==0) return string(1,s[w]);
	string A=calc(x-1,w),B=calc(x-1,(w+1)%3);
	if(A>B) swap(A,B);
	return memo[x][w]=A+B;
}
string solve(){
	cin>>N>>R>>P>>S;
	string ans="z";
	rep(t,3){
		string st=memo[N][t];
		int r=0,p=0,s=0;
		rep(i,st.size()){
			if(st[i]=='P') p++;
			if(st[i]=='R') r++;
			if(st[i]=='S') s++;
		}
		if(p==P&&r==R&&s==S) chmin(ans,st);
	}
	if(ans=="z") ans="IMPOSSIBLE";
	return ans;
}
int main(){
	rep(i,3) calc(13,i);
	int T;
	cin>>T;
	rep1(tt,T){
		printf("Case #%d: ",tt);
		cout<<solve()<<endl;
	}
}
