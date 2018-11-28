#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
using ll = long long;

class range {private: struct I{int x;int operator*(){return x;}bool operator!=(I& lhs){return x<lhs.x;}void operator++(){++x;}};I i,n;
public:range(int n):i({0}),n({n}){}range(int i,int n):i({i}),n({n}){}I& begin(){return i;}I& end(){return n;}};

void solve();

int main() {
  int T; cin >> T;
  for (int t : range(1, T+1)) {
    cout << "Case #" << t << ": ";
    solve();
  }
}

//=====

void solve() {
  int N; cin >> N;

  vector<int> v(N);
  for (int i : range(N)) cin >> v[i];

  int ret = 1 << 30;
  for (int e : range(1, 2000)) {
    int cand = e;
    for (int& x : v) cand += (x - 1) / e;
    ret = min(ret, cand);
  }

  cout << ret << endl;
}
