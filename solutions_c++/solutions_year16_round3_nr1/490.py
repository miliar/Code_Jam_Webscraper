
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

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

template <class T>
using heap = priority_queue<T, vector<T>>;

string solve(heap<pair<int,char>>& parties) {
  string ans;
  while (!parties.empty()) {
    auto p = parties.top(); parties.pop();
    ans.push_back(p.second);
    if (p.first > 1) parties.push(make_pair(p.first-1, p.second));
  }
  return ans;
}

int main() {
  int TC;
  cin >> TC;
  for (int tc=0; tc<TC; tc++) {
    int N, x;
    cin >> N;
    heap<pair<int,char>> parties;
    for (int i=0; i<N; i++) {
      cin >> x;
      parties.push( make_pair(x,'A' + i));
    }
    string ans = solve(parties);
    cout << "Case #" << tc+1 << ": ";
    if (ans.size() & 1) cout << ans[0] << " ";
    for (unsigned int i=ans.size()&1; i<ans.size(); i+=2) {
      for (unsigned int j=0; j<2 && (i+j)<ans.size(); j++) {
        cout << ans[i+j];
      }
      cout << " ";
    }
    cout << endl;
  }
}
