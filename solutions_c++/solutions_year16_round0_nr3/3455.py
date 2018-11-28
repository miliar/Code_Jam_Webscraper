#include "bits/stdc++.h"
using namespace std;
#define LIM
#define MOD
#define gc                       getchar_unlocked
#define ll                       long long
#define pb                       push_back
#define fi                       first
#define se                       second
#define mp                       make_pair
#define TA(a,n)                  for(int i=0;i<n;i++)  cout<<a[i]<<" "; cout<<endl;
#define TM(a,n,m)                for(int i=0;i<n;i++) { for(int j=0;j<m;j++)  cout<<a[i][j]<<" "; cout<<endl; }
#define TP(a,n)                  for(int i=0;i<n;i++)  cout<<a[i].first<<" "<<a[i].second<<endl;
#define all(v)                   v.begin(),v.end()
#define uniq(v)                  sort(all(v));  v.erase(unique(all(v)),v.end())
#define FOR(i,n,m)               for(int i=0;i<n;i+=m)
#define For(i,n,m)               for(int i=1;i<=n;i+=m)
#define CB(value)                __builtin_popcount(value)
#define TB0(value)               __builtin_ctz(value)
#define LB0(value)               __builtin_clz(value)
#define clr(x,val)               memset(x,val,sizeof(x))
#define __                       int t; scanf("%d",&t); while(t--)
const double pi=acos(-1.0);
template<typename T> T max(T a, T b) {if(a>=b) return a; return b;}
template<typename T> T min(T a, T b) {if(a<=b) return a; return b;}
template<typename T> T gcd(T a, T b) {if(!b) return a;return gcd(b, a % b);}
template<typename T> T lcm(T a, T b) {return a * b / gcd(a, b);}
int a[1000002];
ll div_1[11][17];
int divisor(ll x){
	int n=sqrt(x);
	for(int i=2;i<=n;i++){
		if(x%i==0) return i;
	}
}
int prime(ll x){
	int flag=0;
	for(int i=2;i<=sqrt(x);i++){
		if(x%i==0) { flag=1; break; }
	}
	if(flag) return 0;
	else return 1;
}
int main(){
  //ios_base::sync_with_stdio(false); cin.tie(NULL);
  #ifdef DEBUG
    freopen("E:\CodeStack\input.txt", "w", stdout);
    assert(freopen("E:\CodeStack\output.txt", "r", stdin));
  #endif
  FOR(i,11,1){
    FOR(j,17,1){
       div_1[i][j]=pow(i,j);
    }
  }
  //TM(div_1,11,17);
  __{
  cout<<"Case #1: "<<endl;
  int n,j;
  cin>>n>>j;
  int sz=pow(2,n);
  FOR(k,sz,1){
    if(k%2==1){
  	int bit[20];
  	clr(bit,0);
  	int u=0;
  	int d=k;
  	while(d){
  		bit[u++]=d%2;
  		d/=2;
  	}
  	bit[0]=1;
  	bit[n-1]=1;
  	//TA(bit,n);
  	int flag=0;
  	vector<ll> ans;
  	for(int i=2;i<=10;i++){
  		ll ans_1=0;
  		FOR(j,n,1){
  			ans_1+=(bit[j]*div_1[i][j]);
  		}
  		//cout<<ans_1<<" ";
  		if(prime(ans_1)==1 || ans_1==1 || ans_1==0) { flag=1; break; }
  		else ans.pb(ans_1);
  	}
  	//cout<<endl;
  	if(flag==0){
  		j--;
  		for(int i=n-1;i>=0;i--){
  			cout<<bit[i];
  		}
  		cout<<" ";
  		FOR(i,ans.size(),1){
  			cout<<divisor(ans[i])<<" ";
  		}
  		cout<<endl;
  	}
  	if(j==0) break;
  }
  }
  }
return 0;
}
