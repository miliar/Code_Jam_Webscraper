#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

int N, M;
string A[1010];

#define MOD 1000000007

int lcp(string A, string B) {
  int res = 0;
  for(; res < A.size() && res < B.size(); res++) {
    if(A[res] != B[res]) break;
  }
  return res;
}

string last[10];

pair<int, int> solve(int x) {
  if(x == M) return make_pair(0, 1);

  pair<int, int> res(-1, 0);
  for(int i = 0; i < N; i++) {
    int cst = A[x].size() - lcp(A[x], last[i]);
    if(last[i].empty()) {
      cst++;
    }

    string tmp = A[x];
    swap(tmp, last[i]);

    pair<int, int> nres = solve(x + 1);
    nres.first += cst;

    if(nres.first == res.first) {
      res.second += nres.second;
    } else if(nres.first > res.first) { 
      res = nres;
    }

    swap(tmp, last[i]);
  }
  return res;
}


int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> M >> N;
    for(int i = 0; i < M; i++) {
      cin >> A[i];
    }
    sort(A, A + M);

    pair<int, int> res = solve(0);
    int res1 = res.first;
    int res2 = res.second;

    printf("Case #%d: %d %d\n", t, res1, res2);
  }
  return 0;
}
