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
#define rrep(X,Y) for (int (X) = (Y-1);(X) >=0;--(X))
#define repe(X,Y) for ((X) = 0;(X) < (Y);++(X))
#define peat(X,Y) for (;(X) < (Y);++(X))
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
template<class T> using vv=vector<vector<T>>;
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"{"; rep(i,t.size()) {os<<t[i]<<",";} os<<"}"<<endl; return os;}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}

string dirs="^<v>";

int main(){
  ios_base::sync_with_stdio(false);
  cout<<fixed<<setprecision(0);
  int i,j,k,T;
  cin>>T;
  rep(cases,T){
    int n,m;
    cin>>n>>m;
    vector<string> mp(n);
    vv<int> v(n,vector<int>(m));
    rep(i,n)
      cin>>mp[i];
    rep(x,m){
      rep(y,n)if(mp[y][x]!='.'){
	v[y][x]|=1; break;
      }
      rrep(y,n)if(mp[y][x]!='.'){
	v[y][x]|=(1<<2); break;
      }
    }
    rep(y,n){
      rep(x,m)if(mp[y][x]!='.'){
	v[y][x]|=(1<<1); break;
      }
      rrep(x,m)if(mp[y][x]!='.'){
	v[y][x]|=(1<<3); break;
      }
    }
    int re=0,f=0;
    //cout<<v;
    rep(y,n)rep(x,m){
      if(v[y][x]==15){f=1;break;}
      rep(i,4)if(mp[y][x]==dirs[i]){
	if(v[y][x]>>i&1)++re;
      }
    }
    cout<<"Case #"<<cases+1<<": ";
    if(f)
      cout<<"IMPOSSIBLE"<<endl;
    else
      cout<<re<<endl;
  }
  return 0;
}
