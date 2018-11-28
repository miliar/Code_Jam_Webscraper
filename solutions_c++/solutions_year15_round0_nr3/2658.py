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
typedef long long ll;
int a[8][8]={
	{0,1,2,3},
	{1,4,3,6},
	{2,7,4,1},
	{3,2,5,4}
};
int ex(int x,ll p){
	int r=0;
	while(p){
		if(p%2) r=a[r][x];
		x=a[x][x];
		p/=2;
	}
	return r;
}
bool solve(string s){
	int x=0;
	rep(i,s.size()){
		x=a[x][s[i]-'h'];
	}
	if(x!=4) return 0;
	x=0;
	int le=1e8;
	rep(i,s.size()){
		x=a[x][s[i]-'h'];
		if(x==1){
			le=i;
			break;
		}
	}
	x=0;
	int ri=-1e8;
	for(int i=s.size()-1;i>=0;i--){
		x=a[s[i]-'h'][x];
		if(x==3){
			ri=i;
			break;
		}
	}
	if(le<ri) return 1;
	return 0;
}
int main(){
	int T;
	cin>>T;
	rep(i,4) rep(j,4){
		a[i][j+4]=a[i+4][j]=(a[i][j]+4)%8;
		a[i+4][j+4]=a[i][j];
	}
	rep1(tt,T){
		int L;
		ll X;
		string t;
		cin>>L>>X>>t;
		string s;
		rep(i,X) s+=t;
		printf("Case #%d: ",tt);
		if(solve(s)) puts("YES");
		else puts("NO");
	}
}
