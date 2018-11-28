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

double dp[2][44];

int main(){
  ios_base::sync_with_stdio(false);
  cout<<fixed<<setprecision(10);
  int T;
  cin>>T;
  rep(test,T){
    int n,t;
    cin>>n>>t;
    vector<double> ps(n);
    rep(i,n) cin>>ps[i];
    //cout<<ps;
    double re=0;
    rep(i,1<<n)if(__builtin_popcount(i)==t){
      fill(dp[0],dp[0]+2*44,0.);
      double *cur=dp[0],*nxt=dp[1];
      cur[22]=1;
      rep(j,n)if(i>>j&1){
	fill(nxt,nxt+44,0);
	reps(k,1,43){
	  nxt[k-1]+=cur[k]*(1-ps[j]);
	  nxt[k+1]+=cur[k]*ps[j];
	}
	swap(nxt,cur);
	//reps(k,18,25)cout<<cur[k]<<",";cout<<endl;
      }
      MX(re,cur[22]);
    }
    // rep(i,n){
    //   rrep(j,n) reps(k,1,43){
    // 	MX(dp[j+1][k],dp[j][k-1]*ps[i]+dp[j][k+1]*(1-ps[i]));
    //   }
    //   cout<<"["<<i<<"]"<<endl;
    //   rep(j,n+1){reps(k,19,25)cout<<dp[j][k]<<",";cout<<endl;}
    //}
    cout<<"Case #"<<test+1<<": "<<re<<endl;
  }
  return 0;
}
