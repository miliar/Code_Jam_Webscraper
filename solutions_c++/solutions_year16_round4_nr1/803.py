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
#define LARGE(X,Y) X>Y?Y+X:X+Y

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

int main(){
  ios_base::sync_with_stdio(false);
  cout<<fixed<<setprecision(0);
  int T;
  cin>>T;
  rep(test,T){
    int x,y,z,N,no=0;
    cin>>N>>x>>z>>y;
    vector<string> r(x,"R"),s(y,"S"),p(z,"P"),r_,s_,p_;
    //cout<<x<<r<<y<<s<<z<<p;
    rep(i,N){
      r_=r; s_=s; p_=p;
      r.clear(); s.clear(); p.clear();
      int t=x+y-z;
      if(t%2 || t<0 || min(x,y)<t/2){
	no=1;
	break;
      }
      t/=2;
      rep(i,t){
	r.pb(LARGE(r_.back(),s_.back()));
	r_.pop_back(); s_.pop_back();
      }
      rep(i,y-t){
	s.pb(LARGE(s_.back(),p_.back()));
	p_.pop_back(); s_.pop_back();
      }
      rep(i,x-t){
	p.pb(LARGE(p_.back(),r_.back()));
	r_.pop_back(); p_.pop_back();
      }
      x=r.size(); y=s.size(); z=p.size();
      sort(all(r)); sort(all(s)); sort(all(p));
      //cout<<x<<r<<y<<s<<z<<p;
    }
    cout<<"Case #"<<test+1<<": ";
    if(no){
      cout<<"IMPOSSIBLE"<<endl;
    }else{
      if(r.size()) cout<<r[0]<<endl;
      if(s.size()) cout<<s[0]<<endl;
      if(p.size()) cout<<p[0]<<endl;
    }
  }
  return 0;
}
