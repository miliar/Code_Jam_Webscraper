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
void solve(){
	string s;
	int K;
	cin>>s>>K;
	int N=s.size();
	int ans=0;
	rep(i,N-K+1){
		if(s[i]=='-'){
			rep(j,K) s[i+j]^=('+'^'-');
			ans++;
		}
	}
	rep(i,N) if(s[i]=='-'){
		puts("IMPOSSIBLE");
		return;
	}
	cout<<ans<<endl;
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		solve();
	}
}
