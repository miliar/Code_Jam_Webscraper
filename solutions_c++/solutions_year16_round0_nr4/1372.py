

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
  a << "{";
  if (v.size()>0) a << v[0];
  for (int i=1; i<v.size(); i++) a << ", " << v[i];
  a << "}";
  return a;
}

LL my_pow(LL a, LL b) {
  if (b==0) return 1;
  LL tmp = my_pow(a, b/2);
  tmp = tmp*tmp;
  if (b&1) tmp = tmp*a;
  return tmp;
}

vector<LL> solve(int K, int C) {
  vector<LL> ans;
  if (C == 1 || K == 1) {
    for (int i=1; i<=K; i++) ans.push_back(i);
  } else {
    LL gsize = my_pow(K, C-1);
    for (int curr=0; curr<K; curr+=2) {
      LL offset = curr*gsize;
      LL query;
      if (curr==(K-1)) {
        //we had odd number of tiles, the last one accouns only for itself
        query = K*gsize;
      } else {
        query = offset+(curr+1)+1; //Query me and next
      }
      ans.push_back(query);
    }
  }
  return ans;
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  int K, C, S;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    cin >> K >> C >> S;
    vector<LL> ans = solve(K,C);
    cout << "Case #" << tc << ":";
    if (ans.size() > S) {
      cout << " IMPOSSIBLE" << endl;
    } else {
      for (auto x : ans) {
        cout << " " << x;
      }
      cout << endl;
    }
  }
}
