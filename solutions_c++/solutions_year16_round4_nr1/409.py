#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

char ch[4] = "RSP";

string work(int n, int id) {
  if (n == 0) {
    string t = "";
    t = ch[id];
    return t;
  }
  else {
    string a = work(n - 1, id);
    string b = work(n - 1, (id + 1) % 3);
    if (a < b) return a + b;
    return b + a;
  }
}

int N, R, P, S;
int c[5];
string solve() {
  c[0] = c[1] = c[2] = 0;
  for (int i = 0; i < (1<<N); i++) {
    c[__builtin_popcount(i) % 3]++;
  }
  string ans = "";
  for (int i = 0, j = 0; i < 3; i++, j--) {
    if (R == c[i] && S == c[(i+1)%3] && P == c[(i+2)%3]) {
      string tmp = work(N, (j+3)%3);
      if (ans.length() == 0) ans = tmp;
      else if (tmp < ans) ans = tmp;
    }
  }
  if (ans.length() == 0) return "IMPOSSIBLE";
  else return ans;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int kase = 1; kase <= T; kase++) {
    scanf("%d%d%d%d", &N, &R, &P, &S);
    printf("Case #%d: ", kase);
    cout << solve() << endl;
  }

  return 0;
}
