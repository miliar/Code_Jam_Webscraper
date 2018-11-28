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
int arr[1000];
int main(){
	cin>>T;
	rep(tt,T){
		int a=0;
		cin>>n;
		vector<int> vec;
		rep(i,n){
			cin>>arr[i];
			vec.PB(i);
		}
		ll ans=INF;
		do{
			int flg=0;
			int nw=-1;
			rep(i,n){
				if(flg==1&&nw<arr[vec[i]]){
					flg=-1;break;
				}else if(flg==0&&nw<arr[vec[i]]){
					nw=arr[vec[i]];
				}else if(flg==0){
					nw=arr[vec[i]];
					flg=1;
				}else{
					nw=arr[vec[i]];
				}
			}
			
			if(flg==-1)continue;
			int t=0;
			rep(i,n){
				for(int j=i+1;j<n;j++){
					if(vec[i]>vec[j])t++;
				}
			}
			ans=min(ans,(ll)t);
		}while(next_permutation(vec.begin(), vec.end()));
		printf("Case #%d: %lld\n",tt+1,ans);
	}
	return 0;
}
