#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using VI = vector<int>;
using VLL = vector<ll>;
using VS = vector<string>;

enum { R, P, S};
const VI other{S, R, P};
const string names = "RPS";

void build(int n, int root, VI &num, string &s) {
  if (n == 0) {
    --num[root];
    s = names[root];
    return;
  }
  VS vs(2);
  build(n-1, root, num, vs[0]);
  build(n-1, other[root], num, vs[1]);
  sort(vs.begin(), vs.end());
  s = vs[0] + vs[1];
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int T; cin >> T;
  for (int ncase = 1; ncase <= T; ++ncase) {
    int n; cin >> n;
    int r, p, s; cin >> r >> p >> s;
    VS answers;
    for (int i = 0; i < 3; ++i) {
      int root = i;
      VI num{r,p,s};
      string str;
      build(n, root, num, str);
      bool valid = true;
      for (int j = 0; j < 3; ++j) {
        if (num[j]) valid = false;
      }
      if (valid) answers.push_back(str);
    }
    if (answers.empty()) answers = {"IMPOSSIBLE"};
    sort(answers.begin(), answers.end());
    cout << "Case #" << ncase << ": " << answers[0] <<  endl;
  }
}
