#include <iostream>

using namespace std;

int main() {
  auto solve = [](int n) {
    if (n == 0)
      return -1;
    
    bool seen[10] = {};
    int seen_cnt = 0;

    auto mark_digits = [&](int x) {
      while (x != 0) {
	int d = x % 10;
	x /= 10;
	
	if (seen[d])
	  continue;
	++seen_cnt;
	seen[d] = true;
      }
    };

    int current = n;
    while (true) {
      mark_digits(current);
      if (seen_cnt == 10)
	return current;
      current += n;
    };

    return current;
  };

  int cases;
  cin >> cases;

  for (int c = 1; c <= cases; ++c) {
    int n;
    cin >> n;

    cout << "Case #" << c << ": ";

    int res = solve(n);
    if (res == -1)
      cout << "INSOMNIA";
    else
      cout << res;

    cout << "\n";
  }
}
