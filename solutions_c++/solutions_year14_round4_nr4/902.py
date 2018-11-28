#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

int ret, ret_cnt;

struct Trie {
  int value;
  Trie *next[0x100];
  Trie(){ value = 0; fill(next, next+0x100, (Trie*)0); }
  ~Trie(){
    Trie *r = this;
    for(int i=0; i<0x100; i++){
      if(r->next[i]) delete r->next[i];
    }
  }
  void insert(const string &str){
    Trie *r = this;
    for(int i=0; i<str.length(); i++){
      if(!r->next[str[i]]) r->next[str[i]] = new Trie;
      r = r->next[str[i]];
      r->value++;
    }
  }
  int nodecount(){
    Trie *r = this;
    int res = 0;
    for(int i=0; i<0x100; i++){
      if(r->next[i]){
        res += r->next[i]->nodecount();
      }
    }
    return res + (value>0);
  }
};

int nodecount(const vector<string>& w){
  Trie trie;
  trie.value = 1;
  rep(i,w.size()){
    trie.insert(w[i]);
  }
  return trie.nodecount();
}

void check(int N, const vector<string>& v, const vector<int>& s){
  set<int> ss;
  rep(i,s.size()) ss.insert(s[i]);
  if(ss.size() != N) return;

  //rep(i,s.size()) cerr << s[i] << " "; cerr << endl;
  
  int res = 0;
  rep(i,N){
    vector<string> w;
    rep(j,s.size()){
      if(s[j] == i){
        w.push_back(v[j]);
      }
    }
    res += nodecount(w);
  }
  cerr << "\t" << res << endl;
  
  if(ret < res){
    ret = res;
    ret_cnt = 1;
  }
  else if(ret == res){
    ret_cnt++;
  }
}
bool inc(int N, vector<int>& s){
  int i = 0;
  while(i<s.size()){
    s[i]++;
    if(s[i]==N){
      s[i] = 0;
      i++;
    }else{
      break;
    }
  }

  bool flg = true;
  rep(i,s.size()){
    if(s[i] != 0) flg = false;
  }
  return flg;
}


void solve(int N, vector<string>& v){
  ret = -1;
  ret_cnt = 0;
  
  vector<int> s(v.size(), 0);
  while(true){
    check(N, v, s);
    if(inc(N, s)) break;
  }
}

int main(){
  int T;
  cin >> T;

  for(int t=0; t<T; t++){
    int N, M;
    cin >> M >> N;
    string str;
    vector<string> v;
    rep(i,M){
      cin >> str;
      v.push_back(str);
    }
    solve(N, v);
    
    cout << "Case #" << t+1 << ": " << ret << " " << ret_cnt << endl;
  }
  
  return 0;
}
