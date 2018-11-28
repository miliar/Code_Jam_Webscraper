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
bool can(int X,int H,int W){
	if(X>=7) return 0;
	if(H*W%X) return 0;
	if(H<W) swap(H,W);
	if(H<X) return 0;
	if(W<(X+1)/2) return 0;
	if(X==1){
		return 1;
	}
	if(X==2){
		return 1;
	}
	if(X==3){
		return 1;
	}
	if(X==4){
		if(W==2){
			return 0;
		}else{
			return 1;
		}
	}
}
int main(){
	int T;
	cin>>T;
	rep1(tt,T){
		int x,h,w;
		cin>>x>>h>>w;
		printf("Case #%d: ",tt);
		if(can(x,h,w)) puts("GABRIEL");
		else puts("RICHARD");
	}
}
