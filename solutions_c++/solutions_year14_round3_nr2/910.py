#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

#define REP(i, n) for (int i = 0; i < (n); i++)

std::vector<std::pair<int, std::string> > sets;

bool is_valid(const std::string &s) {
  bool seen[30] = { false };
  for (int i = 0; i < s.length(); i++) {
    if (seen[s[i] - 'a'] && s[i] != s[i - 1]) {
      return false;
    }

    seen[s[i] - 'a'] = 1;
  }
  return true;
}

void docase(int tcase) {
  sets.clear();

  int n; scanf("%d", &n);
  int size = 0;
  for (int i = 0; i < n; i++) {
    char buf[1000];
    scanf("%s", buf);
    sets.push_back(std::make_pair(i, std::string(buf)));
    size += strlen(buf);
  }

  std::sort(sets.begin(), sets.end());

  unsigned long long int ways = 0LL;
  do {
    std::string str; str.reserve(size);
    for (int i = 0; i < sets.size(); i++) {
      str += sets[i].second;
    }

    if (is_valid(str))
      ++ways;

  } while (std::next_permutation(sets.begin(), sets.end()));

  printf("Case #%d: %llu\n", tcase, ways);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; i++) docase(i+1);
}
