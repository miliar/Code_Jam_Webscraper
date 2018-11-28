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
void fix(double &x){
	if(abs(x)<1e-9) x=0;
}
void solve(){
	int N;
	double X,V,r[2],c[2];
	cin>>N>>V>>X;
	rep(i,N) cin>>r[i]>>c[i];
	if(N==1){
		if(X==c[0]){
			printf("%.12f\n",V/r[0]);
		}else{
			puts("IMPOSSIBLE");
		}
		return;
	}
	if(c[0]==c[1]){
		if(X==c[0]){
			printf("%.12f\n",V/(r[0]+r[1]));
		}else{
			puts("IMPOSSIBLE");
		}
		return;
	}
	double t0=(V*r[1]*c[1]-V*X*r[1])/(r[0]*r[1])/(c[1]-c[0]);
	double t1=(V*r[0]*X-V*c[0]*r[0])/(r[0]*r[1])/(c[1]-c[0]);
	fix(t0),fix(t1);
	if(t0<0||t1<0){
		puts("IMPOSSIBLE");
		return;
	}
	printf("%.12f\n",max(t0,t1));
}
int main(){
	int T;
	cin>>T;
	rep1(tt,T){
		printf("Case #%d: ",tt);
		solve();
	}
}
