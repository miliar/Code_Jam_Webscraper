#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

string Solve(string s) {
  string ret = "";
  for (char c : s) {
    ret = max(c + ret, ret + c);
  }
  return ret;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 0; tc < t; ++tc) {
    char s[1001];
    scanf("%s", s);
    printf("Case #%d: %s\n", tc + 1, Solve(s).c_str());
  }
  return 0;
}
