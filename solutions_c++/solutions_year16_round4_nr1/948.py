#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
using namespace std;

int T, N, R, P, S, mask;
int A[3];
string bases[3] = {"R", "P", "S"};

pair<int, string> dfs(int id, int col, int depth = 0) {
  if (depth == N) {
    if (A[col]) {
      --A[col];
      return make_pair(col, bases[col]);
    } else return make_pair(-1, "");
  } else {
    int choice = (mask >> (id - 1)) & 1;
    int l = (col + choice + 2) % 3;
    int r = (col + choice) % 3;
    auto tl = dfs(id * 2, l, depth + 1);
    auto tr = dfs(id * 2 + 1, r, depth + 1);
    if (tl.first == -1 || tr.first == -1 || tl.first == tr.first) return make_pair(-1, "");
    int w = ((tl.first + 1) % 3 == tr.first) ? tr.first : tl.first;
    string sl = tl.second, sr = tr.second;
    return make_pair(w, (sl < sr) ? (sl + sr) : (sr + sl));
  }
}

int main() {
  scanf("%d", &T);
  REP (tc, T) {
    scanf("%d%d%d%d", &N, &R, &P, &S);

    string ans = "";
    int maxmask = 1 << ((1 << N) - 1);
    for (mask = 0; mask < maxmask; ++mask) {
      FOR (k, 3) {
        A[0] = R, A[1] = P, A[2] = S;
        auto t = dfs(1, k);
        if (t.first != -1) 
          if (ans.empty() || t.second < ans)
            ans = t.second;
      }
    }

    printf("Case #%d: ", tc);
    if (ans.empty()) printf("IMPOSSIBLE\n");
    else printf("%s\n", ans.c_str());
  }
  return 0;
}
