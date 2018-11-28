#include <bits/stdc++.h>

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define iter(a) __typeof(a.begin())
#define FOR(it,a) for(iter(a)it=a.begin();it!=a.end();++it)
#define F first
#define S second
#define SZ(a) (int)((a).size())
#define sz(a) SZ(a)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define ALL(a) (a).begin(),(a).end()
using namespace std;

typedef long long ll;
typedef pair<int,int> PI;
typedef unsigned long long ull;

#ifdef ONLINE_JUDGE
#define PR(...) (void(0))
#else
#define PR(...) do{cerr << "line : " << __LINE__ << ", " << endl; pr(#__VA_ARGS__, __VA_ARGS__);}while(0)
template<class T>
void pr(const string& name, T t){
  cerr << name << ": " << t << endl;
}
template<typename T, typename ... Types>
void pr(const string& names, T t, Types ... rest) {
  auto p = names.find(',');
  cerr << names.substr(0, p) << ": " << t << ", ";
  pr(string(names, p + 1), rest ...);
}
#endif

template<class T,class U> ostream& operator<< (ostream& o, const pair<T,U>& v){return o << "(" << v.F << ", " << v.S << ")";}
template<class T> ostream& operator<< (ostream& o, const vector<T>& v){o << "{";rep(i,SZ(v)) o << (i?", ":"") << v[i];return o << "}";}

template<class T,class U> ostream& operator<< (ostream& o, const map<T,U>& v){o << "{";for(const auto& e : v) o << e << ", ";return o << "}";}
template<class T> ostream& operator<< (ostream& o, const set<T>& v){o << "{";for(const auto& e : v) o << e << ", ";return o << "}";}

template<class T> string to_s(const T& v){ostringstream is;is << v;return is.str();}
//                 <  ^  >  V
const int dx[] = { 0,-1, 0, 1};
const int dy[] = {-1, 0, 1, 0};

#define endl '\n'

ll ei[100000];
ll fi[100000];

vector<ll> ans;
map<ll, ll> app;
int n;



void solve(int ca){
  app.clear();
  cin >> n;
  rep(i, n) cin >> ei[i];
  rep(i, n) cin >> fi[i];
  rep(i, n) app[ei[i]] = fi[i];
  if(app.begin()->F < 0) return;
  ans.clear();
  --app[0];
  int cnt = 0;
  for(int id = 0; id < n; ++id){
    while(app[ei[id]]){
      //if(++cnt > 10) exit(0);
      //PR(id, ei[id], app);
      rep(i, 1 << SZ(ans)){
        ll ts = ei[id];
        rep(j, SZ(ans)) if((i >> j)&1) ts += ans[j];
        --app[ts];
      }
      ans.pb(ei[id]);
    }
  }
  
  
  cout << "Case #" << ca << ":";
  for(auto e : ans) cout << " " << e;
  cout << endl;
}

int main(int argc, char *argv[])
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  rep(i, t) solve(i + 1);
  return 0;
}
