#include<bits/stdc++.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<ll,ll> P;
const ll INF=1000000000;
#define CONST 1000000007
#define EPS (1e-8)
#define PB push_back
#define MP make_pair
#define sz(a) ((int)(a).size())
#define rep(i,n) for(int i=0;i<(int) (n);i++)
#define SORT(a) sort((a).begin(),(a).end())
ll mod(ll a,ll m){return (a%m+m)%m;}
int dx[9]={0,1,0,-1,1,1,-1,-1,0},dy[9]={1,0,-1,0,1,-1,1,-1,0};
ll n,m,T;
ll cnt,ans;
vector <string> vec;
int g[10];
void dfs(int x){
	if(x==m){
		set<string> st[4];
		rep(i,m){
			rep(j,vec[i].length()){
				//cout<<vec[i].substr(0,j+1)<<endl;
				st[g[i]].insert("");
				st[g[i]].insert(vec[i].substr(0,j+1));
			}
		}
		ll num=0;
		rep(i,4){
			num+=st[i].size();
		}
		if(num>ans){
			ans=num;cnt=1;
		}else if(num==ans){
			cnt++;cnt=cnt%1000000007;
		}
	}else{
		rep(i,n){
			g[x]=i;
			dfs(x+1);
		}
	}
}
int main(){
	cin>>T;
	rep(tt,T){
		ans=0;
		cnt=0;
		vec.clear();
		cin>>m>>n;
		rep(i,m){
			string s;
			cin>>s;
			vec.PB(s);
		}
		dfs(0);
		printf("Case #%d: %lld %lld\n",tt+1,ans,cnt);
	}
	return 0;
}
