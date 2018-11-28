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
int main(){
  //ios_base::sync_with_stdio(false); cin.tie(NULL);
  #ifdef DEBUG
    freopen("E:\CodeStack\input.txt", "w", stdout);
    assert(freopen("E:\CodeStack\output.txt", "r", stdin));
  #endif
  int y=1;
  __{
  	string s;
  	cin>>s;
  	int ans=0;
  	FOR(i,s.size(),1){
  		if(s[i]=='+' && s[i+1]=='-' && i+1<s.size()){
  			ans++;
  		}
  		if(s[i]=='-'){
  			ans++;
  			while(s[i]=='-' && i<s.size()) i++;
  			i--;
  		}
  	}
  	cout<<"Case #"<<y++<<": "<<ans<<endl;
  }
return 0;
}
