#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <functional>
#include <set>
#include <ctime>
#include <random>
#include <chrono>
#include <cassert>
using namespace std;

namespace {
  using Integer = long long; //__int128;
  template<class T> istream& operator >> (istream& is, vector<T>& vec){for(T& val: vec) is >> val; return is;}
  template<class T> istream& operator ,  (istream& is, T& val){ return is >> val;}
  template<class T> ostream& operator << (ostream& os, const vector<T>& vec){for(int i=0; i<vec.size(); i++) os << vec[i] << (i==vec.size()-1?"":" "); return os;}
  template<class T> ostream& operator ,  (ostream& os, const T& val){ return os << " " << val;}

  template<class H> void print(const H& head){ cout << head; }
  template<class H, class ... T> void print(const H& head, const T& ... tail){ cout << head << " "; print(tail...); }
  template<class ... T> void println(const T& ... values){ print(values...); cout << endl; }

  template<class H> void eprint(const H& head){ cerr << head; }
  template<class H, class ... T> void eprint(const H& head, const T& ... tail){ cerr << head << " "; eprint(tail...); }
  template<class ... T> void eprintln(const T& ... values){ eprint(values...); cerr << endl; }

  string operator "" _s (const char* str, size_t size){ return move(string(str)); }
  constexpr Integer my_pow(Integer x, Integer k, Integer z=1){return k==0 ? z : k==1 ? z*x : (k&1) ? my_pow(x*x,k>>1,z*x) : my_pow(x*x,k>>1,z);}
  constexpr Integer my_pow_mod(Integer x, Integer k, Integer M, Integer z=1){return k==0 ? z%M : k==1 ? z*x%M : (k&1) ? my_pow_mod(x*x%M,k>>1,M,z*x%M) : my_pow_mod(x*x%M,k>>1,M,z);}
  constexpr unsigned long long operator "" _ten (unsigned long long value){ return my_pow(10,value); }

  inline int k_bit(Integer x, int k){return (x>>k)&1;} //0-indexed

  mt19937 mt(chrono::duration_cast<chrono::nanoseconds>(chrono::steady_clock::now().time_since_epoch()).count());

  template<class T> string join(const vector<T>& v, const string& sep){
    stringstream ss; for(int i=0; i<v.size(); i++){ if(i>0) ss << sep; ss << v[i]; } return ss.str();
  }

  long long gcd(long long a, long long b){ return (b==0)?a:gcd(b,a%b); }
  template<class ... T> long long gcd(long long a, long long b, T ... c){ return gcd(gcd(a,b), c...);}
  long long lcm(long long a, long long b){ if(a<b) swap(a,b); return (b==1)?a:a*(b/gcd(a,b)); }
  template<class ... T> long long lcm(long long a, long long b, T ... c){ return lcm(lcm(a,b), c...);}
  
}

constexpr long long mod = 9_ten + 7;


void solve(){
  int n;
  cin >> n;
  int r,p,s;
  cin >> r,p,s;

  string ans;
  ans += 'Z';

  //[R,P,S]

map<pair<char,int>,vector<int>> memo;
map<pair<char,int>, string> memo2;
  function<vector<int>(char,int)> dfs = [&](char c, int d) -> vector<int>{
    if(memo.find({c,d}) != memo.end()) return memo[{c,d}];

    if(d==0){
      if(c=='R'){
        return {1,0,0};
      }else if(c=='P'){
        return {0,1,0};
      }else if(c=='S'){
        return {0,0,1};
      }
    }
    vector<int> a,b;
    if(c=='R'){
      a = dfs('R', d-1);
      b = dfs('S', d-1);
    }else if(c=='P'){
      a = dfs('P', d-1);
      b = dfs('R', d-1);
    }else if(c=='S'){
      a = dfs('S', d-1);
      b = dfs('P', d-1);
    }
    for(int i=0; i<3; i++){
      a[i] += b[i];
    }
    memo[{c,d}] = a;
    return a;
  };


  function<string(char,int)> dfs2 = [&](char c, int d) -> string{
    if(memo2.find({c,d}) != memo2.end()) return memo2[{c,d}];

    if(d==0){
      if(c=='R'){
        return "R";
      }else if(c=='P'){
        return "P";
      }else if(c=='S'){
        return "S";
      }
    }
    string a,b;
    if(c=='R'){
      a = dfs2('R', d-1);
      b = dfs2('S', d-1);
    }else if(c=='P'){
      a = dfs2('P', d-1);
      b = dfs2('R', d-1);
    }else if(c=='S'){
      a = dfs2('S', d-1);
      b = dfs2('P', d-1);
    }
    if(a<b) a = a+b;
    else    a = b+a;
    memo2[{c,d}] = a;
    return a;
  };

  for(char c : {'R','P','S'}){
    auto res = dfs(c, n);

    if(res != vector<int>{r,p,s}) continue;

    auto tmp = dfs2(c, n);
    if(ans > tmp) ans = tmp;
  }


  if(ans == "Z"){
    print("IMPOSSIBLE");
  }else{
    print(ans);
  }
}

int main(){
  int t;
  cin >> t;
  for(int i=0; i<t; i++){
    print("Case #");
    print(i+1);
    print(": ");
    solve();
    puts("");
  }
  return 0;
}
