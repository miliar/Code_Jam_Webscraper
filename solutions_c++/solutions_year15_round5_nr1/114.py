#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

long long S[1024000], M[1024000];
int p[1024000];
vector<int> g[1024000];
int flag[1024000];

long long res, sum;

void addDfs(int v) {
}

void addNode(int v) {
  flag[v] = 1;
  vector<int> vec;
  if (p[v] == -1 || flag[p[v]] == 2) vec.push_back(v);
  while (!vec.empty()) {
    int v = vec.back(); vec.pop_back();
    if (flag[v] == 1) {
      flag[v] = 2;
      ++sum;
      res = max(res, sum);
      for (int i: g[v]) vec.push_back(i);
    }
  }
}

void deleteDfs(int v) {
}

void deleteNode(int v) {
  //cout << "delete " << v << endl;
  if (flag[v] == 2) {
    vector<int> vec;
    vec.push_back(v);
    while (!vec.empty()) {
      int w = vec.back(); vec.pop_back();
      if (flag[w] == 2) {
        flag[w] = 1; --sum;
        for (int i: g[w]) vec.push_back(i);
      }
    }
  }
  flag[v] = 0;
}

int main() {
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    long long N, D; cin >> N >> D;
    res = 0, sum = 0;
    memset(flag, 0, sizeof(flag));
    REP(i,1024000) g[i].clear();
    long long As, Cs, Rs, Am, Cm, Rm;
    cin >> S[0] >> As >> Cs >> Rs;
    cin >> M[0] >> Am >> Cm >> Rm;
    REP(i,N) {
      S[i+1] = (S[i] * As + Cs) % Rs;
      M[i+1] = (M[i] * Am + Cm) % Rm;
    }
    //REP(i,N) cout << S[i] << " "; cout << endl;
    //REP(i,N) cout << M[i] << " "; cout << endl;
    REP(i,N) {
      if (i == 0) p[i] = -1;
      else { p[i] = M[i] % i; g[p[i]].push_back(i); }
    }
    vector<pair<int,int>> vec;
    REP(i,N) vec.emplace_back(S[i], i);
    sort(ALL(vec));
    for (int l = 0, r = 0; l < N;) {
      long long val = vec[l].first;
      while (r < N && vec[r].first <= val + D) { addNode(vec[r].second); ++r; }
      while (l < N && vec[l].first == val) { deleteNode(vec[l].second); ++l; }
    }
    cout << "Case #" << cas << ": " << res << endl;
  }
  return 0;
}
