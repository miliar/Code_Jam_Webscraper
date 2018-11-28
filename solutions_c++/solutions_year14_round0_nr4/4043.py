#include <cstdio>
#include <algorithm>
#include <vector>

int sz;
std::vector<int> p1, p2;

int war1() {
  std::vector<bool> used(1050, false);
  int result = 0;
  for (int i = sz - 1; i >= 0; --i) {
    bool found = false;
    for (int j = 0; j < sz; ++j) {
      if (used[j]) continue;
      if (p2[j] > p1[i]) {
        used[j] = true;
        found = true;
        break;
      }
    }
    if (!found) {
      ++result;
    }
  }
  return result;
}

int war2() {
  std::vector<bool> used(1050, false);
  int result = 0;

  int low = 0, high = sz - 1; 
  for (int i = 0; i < sz; ++i) {
    if (p1[i] < p2[low]) {
      --high;
    } else {
      ++low;
      ++result;
    }
  }
  return result;
}

void init() {
  scanf("%d", &sz);

  p1.clear();
  p2.clear();
  for (int i = 0; i < sz; ++i) {
    double t;
    scanf("%lf", &t);
    p1.push_back(t*1000000);
  }
  for (int i = 0; i < sz; ++i) {
    double t;
    scanf("%lf", &t);
    p2.push_back(t*1000000);
  }
  std::sort(p1.begin(), p1.end());
  std::sort(p2.begin(), p2.end());
}

int main() {
  int numTest;
  scanf("%d", &numTest);
  for (int i = 0; i < numTest; ++i) {
    init();
    printf("Case #%d: %d %d\n", i + 1, war2(), war1());
  }
}