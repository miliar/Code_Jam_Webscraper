

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <map>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;
typedef pair<char,int> quat;

unordered_map<char,int> position {{'1',0},{'i',1},{'j',2},{'k',3}};

map<tuple<int,quat,int>,bool> dp;
string cat;

quat mul[4][4] = { {{'1',1},{'i',1},{'j',1},{'k',1}},
  {{'i',1},{'1',-1},{'k',1},{'j',-1}},
  {{'j',1},{'k',-1},{'1',-1},{'i',1}},
  {{'k',1},{'j',1},{'i',-1},{'1',-1}}
};

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
    a << "{";
    if (v.size()>0) a << v[0];
    for (int i=1; i<v.size(); i++) a << ", " << v[i];
    a << "}";
    return a;
}

quat operator*(const quat& a, const quat& b) {
  quat ans = mul[position[a.first]][position[b.first]];
  ans.second *= a.second*b.second;
  return ans;
}

string strpow(const string& s, int b) {
  if (b == 0) return string();
  string tmp = strpow(s, b/2);
  tmp = tmp + tmp;
  if (b&1) tmp += s;
  return tmp;
}

bool isPossible(int id, const quat& prod, int part) {
  tuple<int,quat,int> key = make_tuple(id,prod,part);
  if (dp.count(key)) return dp[key];
  if (id == cat.size()) return dp[key] = false;
  quat nextp = prod * quat(cat[id],1);
  if (part == 0) {    
    if (isPossible(id+1, nextp, part)) {
      return dp[key] = true;
    } else if (nextp == quat('i',1)) {
      return dp[key] = isPossible(id+1,quat('1',1), 1);
    } else {
      return dp[key] = false;
    }
  } else if (part == 1) {
    if (isPossible(id+1, nextp, part)) {
      return dp[key] = true;
    } else if (nextp == quat('j',1)) {
      return dp[key] = isPossible(id+1,quat('1',1), 2);
    } else {
      return dp[key] = false;
    }
  } else {
    if (nextp==quat('k',1) && id==(cat.size()-1)) return dp[key] = true;
    return dp[key] = isPossible(id+1,nextp,part);
  }
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC,L,X;
    string str;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> L >> X;
      cin >> str;
      cat = strpow(str,X);
      cout << "Case #" << tc << ": ";
      dp.clear();
      if ( isPossible(0,quat('1',1),0) ) cout << "YES" << endl;
      else cout << "NO" << endl;
    }
}
