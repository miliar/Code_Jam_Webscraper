#include <string>
#include <vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<functional>
#include<list>
#include<deque>
#include<bitset>
#include<set>
#include<map>
#include<unordered_map>
#include<cstring>
#include<sstream>
#include<complex>
#include<iomanip>
#include<numeric>
#define X first
#define Y second
#define pb push_back
#define rep(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define reps(X,S,Y) for (int (X) = S;(X) < (Y);++(X))
#define rrep(X,Y) for (int (X) = (Y)-1;(X) >=0;--(X))
#define repe(X,Y) for ((X) = 0;(X) < (Y);++(X))
#define peat(X,Y) for (;(X) < (Y);++(X))
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()
#define eb emplace_back
#define UNIQUE(X) (X).erase(unique(all(X)),(X).end())

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
template<class T> using vv=vector<vector<T>>;
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"{"; rep(i,t.size()) {os<<t[i]<<",";} os<<"}"<<endl; return os;}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class T> inline bool MX(T &l,const T &r){return l<r?l=r,1:0;}
template<class T> inline bool MN(T &l,const T &r){return l>r?l=r,1:0;}
const ll MOD=1e9+7;

int ok[5][1<<16];
int tb[4][4];
int hd[4],op[4];

int main(){
  ios_base::sync_with_stdio(false);
  cout<<fixed<<setprecision(0);

  ok[1][1]=1;
  reps(i,2,5){
    rep(j,1<<(i*i)){
      rep(p,i) hd[p]=op[p]=0;
      rep(p,i)rep(m,i){
	tb[p][m]=j>>(p*i+m)&1;
	hd[p]|=tb[p][m]<<m;
	op[m]|=tb[p][m]<<p;
      }
      int none=0;
      rep(p,i) if(!hd[p]) none=1;
      if(none) continue;
      int safe=0;
      rep(ms,1<<i)if(ms){
	int f=0;
	rep(k,i) if(ms>>k&1) f|=op[k];
	if(__builtin_popcount(f)<=__builtin_popcount(ms)){
	  //cout<<"ok"<<ms<<","<<f<<endl;
	  rep(k,i) if((ms|hd[k]) == hd[k]) safe|=1<<k;
	  //cout<<safe<<endl;
	}
      }
      if(safe+1==(1<<i)) ok[i][j]=1;
      if(i==2){
	//cout<<ok[i][j]<<endl;
	//rep(x,i){rep(y,i)cout<<tb[x][y]<<",";cout<<endl;}
	//rep(x,i)cout<<hd[x]<<",";cout<<endl;
	//rep(x,i)cout<<op[x]<<",";cout<<endl;
      }
    }
  }

  int T;
  cin>>T;
  rep(test,T){
    int n;
    cin>>n;
    vector<string> str(n);
    rep(i,n) cin>>str[i];
    int st=0;
    rep(i,n)rep(j,n)if(str[i][j]=='1') st|=1<<(i*n+j);
    //cout<<st<<endl;
    int re=n*n;
    rep(i,1<<(n*n)) if((st|i)==i && ok[n][i]) MN(re,__builtin_popcount(i^st));
    //rep(i,1<<(n*n)) if((st|i)==i && ok[n][i]) cout<<i<<":"<<(i^st)<<endl;
    cout<<"Case #"<<test+1<<": "<<re<<endl;
    
  }
  return 0;
}
