#include <iostream>
#include <algorithm>

inline long long calc(int o, int e, int n) {
  return (2 * n + 1 - (e - o)) * (e - o) / 2;
}

int main() {
  int T;
  std::cin >> T;
for (int tt = 1; tt <= T; ++tt) {
  int n, m;
  std::cin >> n >> m;

  int cnt = 0;
  std::pair<int, int> a[10000];

  long long cost = 0;
  for (int i = 0; i < m; ++i) {
    int o, e, p;
    std::cin >> o >> e >> p;
    for (int j = 0; j < p; ++j) {
      a[cnt].first = o;
      a[cnt].second = e;
      ++cnt;
    }

    cost += calc(o, e, n) * p;
  }

  std::sort(a, a + cnt);

  bool flag = true;
  while (flag) {
    flag = false;
    for (int i = 0; i < cnt; ++i) {
      for (int j = i + 1; j < cnt; ++j) {
        if (a[j].first <= a[i].second && a[j].second > a[i].second) {
          std::swap(a[i].second, a[j].second);
          flag = true;
        }
      }
    }
  }

  long long new_cost = 0;
  for (int i = 0; i < cnt; ++i) new_cost += calc(a[i].first, a[i].second, n);

  std::cout << "Case #" << tt << ": " << (cost - new_cost) << std::endl;
}

}
