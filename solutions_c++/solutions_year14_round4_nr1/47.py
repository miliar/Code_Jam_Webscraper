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

int N,X,S[10010];
int used[10010];

void main2(){
	cin>>N>>X;
	rep(i,N)cin>>S[i];
	fill(used,used+N,0);
	sort(S,S+N);
	int ans = 0;
	rep(i,N)if(!used[i]){
		int x = -1;
		for(int j = N-1; j >= i+1; j--){
			if(!used[j] && S[i] + S[j] <= X){
				x = j; break;
			}
		}
		if(x != -1){
			used[x] = 1;
		}
		used[i] = 1;
		ans++;
	}
	cout<<ans<<endl;
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
