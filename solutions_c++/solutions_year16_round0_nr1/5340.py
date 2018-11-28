#include <bits/stdc++.h>


const int maxn = 1000000;

int n = 0;

void solution (int n) {
  if (n == 0) {
    std::cout << "INSOMNIA" << std::endl;
    return ;
  }

  int mask = 0;
  for (int v = n ;  ; v += n) {
    int t = v;
    while (t != 0) {
      int d = t % 10;
      mask |= (1 << d);
      t /= 10;
    }
    if (mask == 1023) {
      std::cout << v << std::endl;
      return ;
    }
  }
}

int main () {
  // std::ios_base::sync_with_stdio(false);

  // std::freopen("x.in", "r", stdin);
  // std::freopen("A-small-attempt0.in", "r", stdin);
  std::freopen("A-large.in", "r", stdin);

  std::freopen("A.out", "w", stdout);

  int T = 0;
  std::cin >> T;
  for (int i = 1 ; i <= T ; i += 1) {
    std::cout << "Case #" << i << ": ";
    int n = 0;
    std::cin >> n;
    solution(n);
  }

  return 0;
}
