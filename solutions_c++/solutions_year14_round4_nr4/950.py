#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;


long long compute(vector<string> &S, int hash) {
  if (S.size() == 0) return 0;
  vector<string> prefixes;
  long long ret = 0;
  for (int ii = 0; ii < S.size(); ii++) {
    string s = S[ii];
    for (int jj = 0; jj < s.size(); jj++) {
      string prefix = s.substr(0, jj+1);
      if (find(prefixes.begin(), prefixes.end(), prefix) == prefixes.end()) {
        ret++;
        prefixes.push_back(prefix);
      }
    }
  }
  return ret+1;
}

void ssolve(vector<string> &S, int M, int N, int *colors, long long &worst, long long &ways) {
  vector<string> servers[N];
  int hash[4] {0};
  for (int ii = 0; ii < M; ii++) {
    servers[colors[ii]].push_back(S[ii]);
    hash[colors[ii]] += 1 << ii;
  }
  long long n = 0;
  for (int ii = 0; ii < N; ii++) {
    n += compute(servers[ii], hash[ii]);
  }
  if (n > worst) {
    worst = n;
    ways = 1;
  }
  else if (n == worst) {
    ways++;
    ways %= 1000000007;
  }
}

void solve(vector<string> &S, int curr, int M, int N, int *colors, long long &total, long long &ways) {
  if (curr == M) {
    ssolve(S, M, N, colors, total, ways);
  }
  else {
    for (int ii = 0; ii < N; ii++) {
      colors[curr] = ii;
      solve(S, curr+1, M, N, colors, total, ways);
    }
  }
}

int main() {
  long long T;
  cin >> T;

  for (long long ii = 1; ii <= T; ii++) {
    cout << "Case #" << ii << ": ";
    long long M, N;
    cin >> M >> N;
    vector<string> S;
    for (int jj = 0; jj < M; jj++) {
      string s;
      cin >> s;
      S.push_back(s);
    }
    int colors[M];
    long long worst = 0, ways = 0;
    solve(S, 0, M, N, colors, worst, ways);
    cout << worst << " " << ways << endl;
  }
}
