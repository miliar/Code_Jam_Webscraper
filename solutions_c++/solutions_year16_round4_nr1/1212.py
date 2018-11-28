#include <algorithm>
#include <cstdio>
#include <string>

char loser(char root) {
  if (root == 'R')
    return 'S';
  else if (root == 'S')
    return 'P';
  else
    return 'R';
}

std::string solve(char root, int level) {
  if (level == 0) return std::string(1, root);
  std::string left = solve(loser(root), level - 1);
  std::string right = solve(root, level - 1);
  return std::min(left + right, right + left);
}

bool ok(std::string str, int r, int p, int s) {
  for (char c : str)
    if (c == 'R')
      r--;
    else if (c == 'P')
      p--;
    else
      s--;
  return !r && !p && !s;
}

int main() {
  int t;
  scanf("%d", &t);

  for (int test = 1; test <= t; test++) {
    int n, r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    std::string result = "ZZZ";
    for (char c : std::string("RPS")) {
      std::string t = solve(c, n);
      if (ok(t, r, p, s)) result = std::min(result, t);
    }
    printf("Case #%d: %s\n", test,
           result == "ZZZ" ? "IMPOSSIBLE" : result.c_str());
  }
}
