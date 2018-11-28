#include <iostream>
#include <cassert>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N, K;
vector<double> P;
vector<double> p1;
double ret = 0;
vector<double> checkProb(vector<double> p) {
  vector<double> ret(p.size() + 1);
  ret[0] = 1;
  for(int i = 0; i < p.size(); i++) {
    vector<double> next(p.size() + 1);
    for(int j = 0; j < ret.size() - 1; j++) {
      next[j] += ret[j] * (1 - p[i]);
      next[j + 1] += ret[j] * (p[i]);
    }
    ret = next;
  }
  return ret;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T;tc++) {
    cout << "Case #" << tc << ": ";
    cin >> N >> K;
    P = vector<double>(N);
    for(int i = 0; i < N; i++) {
      cin >> P[i];
    }
    std::sort(P.begin(), P.end());
    p1.clear();
    ret = 0;
    for(int i = 0; i <= K; i++) {
      p1.clear();
      for(int j = 0; j < i; j++) {
        p1.push_back(P[j]);
      }
      for(int j = N - K + i; j < N; j++) {
        p1.push_back(P[j]);
      }
      vector<double> pp = checkProb(p1);
      assert(p1.size() == K);
      ret = max(ret, pp[K / 2]);
    }
    printf("%.8f\n", ret);
  }
}
