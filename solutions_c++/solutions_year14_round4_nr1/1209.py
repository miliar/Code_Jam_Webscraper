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
int main(){
	cin>>T;
	rep(tt,T){
		vector<ll> arr;
		int a=0,t;
		cin>>n>>m;
		rep(i,n){
			cin>>t;
			arr.PB(t);
		}
		SORT(arr);
		int b=0,e=n-1;
		while(b<=e){
			if(b==e){
				a++;e-=1;b+=1;
			}else if(arr[e]+arr[b]<=m){
				a++;e-=1;b+=1;
			}else{
				a++;e-=1;
			}
		}
		printf("Case #%d: %d\n",tt+1,a);
	}
	return 0;
}
