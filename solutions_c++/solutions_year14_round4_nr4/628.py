#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int T,N,M;
vector<string> W;
map<long long, int> X;

long long pocet(const vector<bool>& v) {
  set<string> S;
  for(int i = 0; i < (int)v.size(); ++i) {
    if (!v[i]) continue;
    for(int j = 0; j <= (int)W[i].size(); ++j) {
      S.insert(string(W[i].begin(), W[i].begin() + j));
    }
  }
  return (long long)S.size();
}

int main() {
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> M >> N;
    W.resize(M);
    X.clear();
    long long Q = 1;
    for(int m = 0; m < M; ++m) {
      Q *= (long long) N;
      cin >> W[m];
    }
    for(long long i = 0; i < Q; ++i) {
      long long q = i;
      vector<vector<bool> > b(N, vector<bool>(M, false));
      for(int j = 0; j < M; ++j) {
        b[q % N][j] = true;
        q /= N;
      }
      
      long long poc = 0;
      bool ok = true;
      for(int j = 0; j < N; ++j) {
        long long p = pocet(b[j]);
        if (p > 0) poc += p;
        else ok = false;
      }

      if (!ok) continue;
      ++X[poc];
    }
    cout << "Case #" << t << ": " << X.rbegin()->first << " " << X.rbegin()->second << endl;
  }
  return 0;
}
