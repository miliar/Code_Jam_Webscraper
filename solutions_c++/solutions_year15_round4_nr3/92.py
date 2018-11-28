#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
#include <sstream>
using namespace std;
using ll = long long;

class range {private: struct I{int x;int operator*(){return x;}bool operator!=(I& lhs){return x<lhs.x;}void operator++(){++x;}};I i,n;
public:range(int n):i({0}),n({n}){}range(int i,int n):i({i}),n({n}){}I& begin(){return i;}I& end(){return n;}};

void solve();

int main() {
  int T; cin >> T;
  for (int test : range(1, T+1)) {
    cout << "Case #" << test << ": ";
    solve();
  }
}

////////////////////////////////////////////////////////////////////////////////

void solve() {
  int N;
  cin >> N;
  string nop; getline(cin, nop);

  int WMax = 5000;
  vector<int> vs[WMax];

  map<string, int> mp;
  for (int i : range(N)) {
    string line; getline(cin, line);
    stringstream ss;
    ss << line;
    string token;
    while (ss >> token) {
      if (!mp.count(token)) {
        int n = mp.size();
        mp[token] = n;
      }
      vs[mp[token]].push_back(i);
    }
  };

  int W = mp.size();

  int ret = 999999;
  for (int bit : range(1 << (N - 2))) {
    int cand = 0;
    for (int i : range(W)) {
      int color = 0;
      for (int x : vs[i]) {
        if (x == 0) color |= 1;
        if (x == 1) color |= 2;
        if (x >= 2) color |= ((bit >> (x - 2)) & 1) ? 1 : 2;
      }

      if (color == 3) cand++;
    }

    ret = min(ret, cand);
  }
  cout << ret << endl;
}
