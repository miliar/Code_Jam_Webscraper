#include <algorithm>
#include <array>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <limits>

static const std::string INSOMNIA = "INSOMNIA";

using ll = long long;

ll count(ll n, ll p, std::array<int, 10>& m) {
  if (n > std::numeric_limits<ll>::max()) {
    return -1;
  }
  for (int x = n; x > 0; x /= 10) {
    int j = x % 10;
    m[j] += 1;
  }
  if (std::all_of(m.begin(), m.end(), [](int i) { return i > 0; })) {
    return n;
  } else {
    return count(n + p, p, m);
  }
}

int main(int argc, char *argv[])
{
  int n;
  std::scanf("%d\n", &n);

  int i;
  std::string result;
  for (int j = 1; j <= n; ++j) {
    std::array<int, 10> m;
    m.fill(0);
    std::scanf("%d\n", &i);
    result += "Case #" + std::to_string(j) + ": ";
    if (i == 0) {
      result += INSOMNIA;
    } else {
      ll c = count(i, i, m);
      result += (c > 0) ? std::to_string(c) : INSOMNIA;
    }
    result += "\n";
  }

  std::cout << result;
  
  return 0;
}
