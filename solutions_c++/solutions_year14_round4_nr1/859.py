#include "cassert"
#include "iostream"
#include "set"

int main() {
  int T, t = 1, N, X;
  for (std::cin >> T; t <= T; ++t) {
    std::cout << "Case #" << t << ": ";
    std::cin >> N >> X;
    std::multiset<int> iset;
    for (int i = 0, s; i < N; ++i) {
      std::cin >> s;
      iset.insert(s);
    }
    int ans = 0, last = 0, c = 0;
    while (!iset.empty()) {
      auto it = iset.upper_bound(last);
      // new a disc
      if (c == 2 || it == iset.begin() || last == 0) {
	last = X;
	++ ans;
	it = iset.upper_bound(last);
	c = 0;
      }
      it = --it;
      assert(last >= *it);
      last -= *it;
      iset.erase(it);
      ++ c;
    }
    std::cout << ans << std::endl;
  }
  return 0;
}
