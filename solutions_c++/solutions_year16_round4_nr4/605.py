#include <algorithm>
#include <cstdio>

const size_t kMaxN = 4;

int g_skills[kMaxN];

int ToMask(int n, char buf[]) {
  int mask = 0;
  for (int i = 0; i < n; ++i) {
    if (buf[i] == '1')
      mask = mask | (1 << i);
  }
  return mask;
}

int PopCount(int mask) {
  int result = 0;
  for (; mask; mask = mask & (mask - 1))
    ++result;
  return result;
}

int Solve(int n) {
  int skills[kMaxN];
  int mask = (1 << n) - 1;

  int best = n * n;

  for (int lessons = 0; lessons < (1 << (n * n)); ++lessons) {
    for (int i = 0; i < n; ++i)
      skills[i] = g_skills[i] | ((lessons >> (n * i)) & mask);
    bool ok = true;
    int all = 0;
    for (int i = 0; i < n && ok; ++i) {
      all = all | skills[i];
      int total = 0;
      for (int j = 0; j < n && ok; ++j) {
        if ((skills[i] & skills[j]) != 0)
          ok = ok && skills[i] == skills[j];
        if (skills[i] == skills[j])
          ++total;
      }
      ok = ok && (total == PopCount(skills[i]));
    }
    ok = ok && (all == mask);
    if (!ok)
      continue;
    if (best > PopCount(lessons))
      best = PopCount(lessons);
  }
  return best;
}

int main() {
  int num_tests;
  scanf("%d", &num_tests);
  for (int test_num = 1; test_num <= num_tests; ++test_num) {
    int n;
    scanf("%d", &n);

    char buf[kMaxN + 1];
    for (int i = 0; i < n; ++i) {
      scanf("%s", buf);
      g_skills[i] = ToMask(n, buf);
    }

    printf("Case #%d: %d\n", test_num, Solve(n));
  }
  return 0;
}
