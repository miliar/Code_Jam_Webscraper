#include <cstdio>

#include <string>
#include <vector>

int solve(int start) {
  if (start == 0) {
    return -1;
  }
  std::vector<int> seen(10, 0);
  int current = start;
  int count = 0;
  while (true) {
    auto s = std::to_string(current);
    for (auto&& digit : s) {
      ++seen[digit - '0'];
    }
    if (std::count(seen.begin(), seen.end(), 0) == 0) {
      fprintf(stderr, "done for %d after %d iterations\n", start, count);
      return current;
    }
    current += start;
    ++count;
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int N;
    scanf("%d", &N);
    int res = solve(N);
    printf("Case #%d: %s\n", t, res == -1 ? "INSOMNIA" : std::to_string(res).c_str());
  }
}
