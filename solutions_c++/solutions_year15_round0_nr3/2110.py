#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <string>
#include <fstream>
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPP(k,a,b) for(int k= (a); k < (b); ++k)
#define INF 200000000
#define mp make_pair
#define len(s) (int)((s).size())
#define pb push_back
#define all(X) (X).begin(), (X).end()
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)

using namespace std;
typedef long long ll;
typedef unsigned int uint;
using vi = vector<int>;
using vii = vector<vector<int>>;
using pii = pair<int,int>;
template <class T>
void print(vector<T> v){ bool first=true; for(T x : v) { if(!first) cout << " "; first = false; cout << x; } cout << endl;}

string mul(const string& q1, const string& q2){
  string sgn="";
  string v1=q1, v2=q2;
  if(q1[0] == '-'){
    v1 = q1[1];
    sgn = "-";
  }
  if(q2[0] == '-'){
    v2 = q2[1];
    sgn = (sgn == "-") ? "" : "-";
  }
  if(v1 == "1") return sgn+v2;
  if(v2 == "1") return sgn+v1;
  if(v1 == "i" && v2 == "i"){
    sgn = (sgn == "-") ? "" : "-";
    return sgn+"1";
  }
  if(v1 == "i" && v2 == "j"){
    return sgn+"k";
  }
  if(v1 == "i" && v2 == "k"){
    sgn = (sgn == "-") ? "" : "-";
    return sgn+"j";
  }
  if(v1 == "j" && v2 == "i"){
    sgn = (sgn == "-") ? "" : "-";
    return sgn+"k";
  }
  if(v1 == "j" && v2 == "j"){
    sgn = (sgn == "-") ? "" : "-";
    return sgn+"1";
  }
  if(v1 == "j" && v2 == "k"){
    return sgn+"i";
  }
  if(v1 == "k" && v2 == "i"){
    return sgn+"j";
  }
  if(v1 == "k" && v2 == "j"){
    sgn = (sgn == "-") ? "" : "-";
    return sgn+"i";
  }
  if(v1 == "k" && v2 == "k"){
    sgn = (sgn == "-") ? "" : "-";
    return sgn+"1";
  }

}

string inv(const string& q){
  if(q == "1" || q == "-1") return q;
  string ans = q[0] == '-' ? string(1,q[1]) : "-"+q;
  return ans;
}
string pow(const string& q, int x){
  if(x == 0) return "1";
  if(x % 2 == 1) return mul(q, pow(q,x-1));
  string q2=pow(q,x/2);
  return mul(q2,q2);
}

int main(){
  int T;
  ifstream fin("c.in");
  ofstream fout("c.out");
  fin >> T;
  REP(t, T){
    int l,x;
    fin >> l >> x;
    string s;
    fin >> s;
    vector<string> M(l+1);
    M[0] = "1";
    REPP(i,1, l+1){
      M[i] = mul(M[i-1], string(1,s[i-1]));
    }
    if(pow(M[l],x) != "-1"){
      fout << "Case #" << (t+1) << ": NO" << endl;
      continue;
    } 
    string ans="NO";
    REP(l1, x){
      if(ans == "YES") break;
      int l2=x-1-l1;
      REP(n, l){
        if(ans == "YES") break;
        string a1=mul(pow(M[l], l1), M[n]);
        if(a1 != "i") continue;
        REPP(r, n+1, l){
          string a2 = mul(inv(M[n]), M[r]);
          string a3 = mul(inv(M[r]), pow(M[l], l2+1));
          if(a1 == "i" && a2 == "j" && a3 == "k"){
            ans = "YES";
            break;
          }
        }
      }
    }
    REP(l1, x-1){
      if(ans == "YES") break;
      REP(r, l){
        if(ans == "YES") break;
        if(mul(pow(M[l], l1), M[r]) != "i") continue;
        REP(l2, x-l1){
          if(ans == "YES") break;
          REP(r2, l){
            if(mul(mul(inv(M[r]), pow(M[l], l2+1)), M[r2]) != "j") continue;
            int l3=x-l1-l2-2;
            if(l3 < 0) continue;
            if(mul(inv(M[r2]), pow(M[l], l3+1)) == "k"){
              ans = "YES";
              break;
            }
          }
        }
      } 
    }
    fout << "Case #" << (t+1) << ": " << ans << endl;
  }
	return 0;
}
