// Enjoy your stay.

#include <bits/stdc++.h>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(auto it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define mt make_tuple
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

typedef istringstream iss;
typedef long long ll;
typedef pair<ll,ll> pi;
typedef stringstream sst;
typedef vector<ll> vi;

ll N,p,q,r,s;
ll a[1000010];
ll sum[1000010];

void main2(){
	cin>>N>>p>>q>>r>>s;
	rep(i,N){
		a[i] = (i * p + q) % r + s;
	}
	sum[0] = 0;
	rep(i,N)sum[i+1] = sum[i] + a[i];
	ll lo = 0, hi = 1e13;
	while(lo + 1 < hi){
		ll mi = lo + hi >> 1;
		int ok = 0;
		int cur = 0;
		ll b = 0;
		while(cur < N && b <= mi){
			b += a[cur++];
		}
		if(cur == N && b <= mi){
			ok = 1;
			goto end;
		}
		cur--;
		b = 0;
		while(cur < N && b <= mi){
			b += a[cur++];
		}
		if(cur == N && b <= mi){
			ok = 1;
			goto end;
		}
		cur--;
		b = 0;
		while(cur < N && b <= mi){
			b += a[cur++];
		}
		if(cur == N && b <= mi){
			ok = 1;
			goto end;
		}
		end:;
		if(ok) hi = mi;
		else lo = mi;
	}
	cout<<fixed<<setprecision(16)<<(sum[N] - hi)*1./sum[N]<<endl;
}

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	
	
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
