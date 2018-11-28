#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
typedef int64_t i64;

struct Solution {
  i64 R, P, S;
  Solution(i64 r, i64 p, i64 s) : R(r), P(p), S(s) {}
};

int main() {
  vector<vector<Solution>> sols(15);
  sols[0] = {Solution(1, 1, 0), Solution(1, 0, 1), Solution(0, 1, 1)};
  for (i64 i = 1; i < sols.size(); i++) {
    for (auto sol : sols[i-1]) {
      sols[i].push_back(Solution(sol.R + sol.P, sol.P + sol.S, sol.R + sol.S));
    }
  }
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    i64 N, R, P, S;
    scanf("%lld %lld %lld %lld", &N, &R, &P, &S);
    printf("Case #%lld: ", zz);
    bool found = false;
    Solution start(0, 0, 0);
    for (i64 i = 0; i < sols[N-1].size(); i++) {
      auto test = sols[N-1][i];
      if (R == test.R && P == test.P && S == test.S) {
        found = true;
        start = sols[0][i];
        break;
      }
    }
    if (!found) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    vector<char> ans;
    if (start.P > 0)
      ans.push_back('P');
    if (start.S > 0)
      ans.push_back('S');
    if (start.R > 0)
      ans.push_back('R');
    vector<char> next;
    for (i64 i = 1; i < N; i++) {
      for (auto c : ans) {
        if (c == 'R') {
          next.push_back('S');
          next.push_back('R');
        } else if (c == 'P') {
          next.push_back('P');
          next.push_back('R');
        } else {
          next.push_back('P');
          next.push_back('S');
        }
      }
      swap(ans, next);
      next.clear();
    }
    for (i64 step = 1; step < ans.size(); step *= 2) {
      for (i64 i = 0; i + step < ans.size(); i += step * 2) {
        bool greater = false;
        for (i64 j = 0; j < step; j++) {
          if (ans[i+j] > ans[i+j+step]) { 
            greater = true;
            break;
          } else if (ans[i+j] > ans[i+j+step]) {
            break;
          }
        }
        if (greater) {
          for (i64 j = 0; j < step; j++) {
            swap(ans[i+j], ans[i+j+step]);
          }
        }
      }
    }
    for (auto ch : ans) {
      printf("%c", ch);
    }
    printf("\n");
  }
}
