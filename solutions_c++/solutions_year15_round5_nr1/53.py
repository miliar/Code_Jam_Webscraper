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

const int MAX_N = 1e6 + 10;

vector<int> G[MAX_N];
int si[MAX_N];
int in[MAX_N];

int dfs(int cv, int a, int b){
  if(si[cv] < a || b < si[cv]) return 0;
  int ret = 1;
  for(auto e : G[cv]) ret += dfs(e, a, b);
  return ret;
}

void solve(int ca){
  int n, d;
  cin >> n >> d;

  rep(i, n) G[i].clear();
  
  {
    ll s0, as, cs, rs;
    cin >> s0 >> as >> cs >> rs;
    rep(i, n){
      si[i] = s0;
      s0 = (s0 * as + cs) % rs;
    }
  }
  {
    ll m0, am, cm, rm;
    cin >> m0 >> am >> cm >> rm;
    rep(i, n){
      if(i){
        int p = m0 % i;
        G[p].pb(i);
      }
      m0 = (m0 * am + cm) % rm;
    }
  }
  int ma = 0;

  set<PI> in;
  set<PI> kouho;
  kouho.insert(mp(si[0],0));
  for(int i = 0; i <= 1000100; ++i){
    bool fl = 0;
    while(!kouho.empty() && kouho.begin()->F <= i + d){
      int cv = kouho.begin()->S;
      kouho.erase(kouho.begin());
      if(si[cv] < i) continue;
      in.insert(mp(si[cv], cv));
      fl = 1;
      for(auto e : G[cv]){
        if(si[e] >= i)
          kouho.insert(mp(si[e],e));
      }
    }
    
    //if(fl) PR(i, in, kouho);
    
    while(!in.empty() && in.begin()->F < i){
      int cv = in.begin()->S;
      queue<int> q;
      q.push(cv);
      fl = 1;
      while(!q.empty()){
        int cv = q.front();
        q.pop();
        if(!in.count(mp(si[cv],cv)) &&
           !kouho.count(mp(si[cv], cv)))
          continue;
        in.erase(mp(si[cv], cv));
        kouho.erase(mp(si[cv], cv));
        for(auto e : G[cv]){
          q.push(e);
        }
      }
    }
    
    //if(fl) PR(i, in);
    
    ma = max(ma, SZ(in));
  }

  cout << "Case #" << ca << ": " << ma << endl;
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
