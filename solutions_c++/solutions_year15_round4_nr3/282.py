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
template<class T> string to_s(const T& v){ostringstream is;is << v;return is.str();}
//                 <  ^  >  V
const int dx[] = { 0,-1, 0, 1};
const int dy[] = {-1, 0, 1, 0};
#define endl '\n'

map<string, int> memo;
int get(string a){
  if(memo.count(a)) return memo[a];
  int sz = SZ(memo);
  return memo[a] = sz;
}

void solve(int ca){
  memo.clear();
  int n;
  cin >> n;
  int ans = 1e9;
  cin.get();
  vector<vector<int> > words(n);
  
  rep(i, n){
    string in;
    getline(cin, in);
    stringstream ss(in);
    while(ss >> in) words[i].pb(get(in));
  }

  vector<int> app(SZ(memo));
  rep(i,n) for(auto e : words[i]) ++app[e];
  
  
  rep(i, 1 << n){
    if((i&1) == ((i >> 1) & 1)) continue;
    vector<int> appe(SZ(memo));
    rep(j, n)
      if((i >> j) & 1)
        for(auto e : words[j]) ++appe[e];
    int tans = 0;
    rep(j, SZ(memo)) tans += (appe[j] && appe[j] < app[j]) ? 1 : 0;
    ans = min(tans, ans);
  }
  
  cout << "Case #" << ca << ": " << ans << endl;
}

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  rep(i, t) solve(i + 1);
  return 0;
}
