#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string let;
vector<int> dep;
vector<vector<int>> pre;

string genrandom(int x) {
  vector<string> v(pre[x].size());
  vector<int> idx(pre[x].size());
  vector<int> perm;
  for (int i = 0; i < pre[x].size(); i++) {
    v[i] = genrandom(pre[x][i]);
    for (int j = 0; j < v[i].size(); j++) perm.push_back(i);
  }

  random_shuffle(perm.begin(), perm.end());
  string ret;
  if (x) ret += let[x];
  for (int i = 0; i < perm.size(); i++) {
    ret += v[perm[i]][idx[perm[i]]++];
  }
  return ret;
}

int main() {
  int T, N, M, prob=1;
  for (cin >> T; T--;) {
    cin >> N;
    dep.resize(N+1);
    pre = vector<vector<int>>(N+1);
    for (int i = 1; i <= N; i++) cin >> dep[i];
    for (int i = 1; i <= N; i++) pre[dep[i]].push_back(i);
    cin >> let;
    let = "?" + let;
    cin >> M;
    vector<string> s(M);
    for (int i = 0; i < M; i++) cin >> s[i];
    printf("Case #%d:", prob++);

    vector<int> found(M);
    for (int i = 0; i < 10000; i++) {
      string t = genrandom(0);
      for (int j = 0; j < s.size(); j++) if (t.find(s[j]) != -1) found[j]++;
    }
    for (int i = 0; i < M; i++) printf(" %.6lf", found[i]/1e4);
    printf("\n");
  }
}
