#include <iostream>
#include <sstream>
#include <string>

using namespace std;

typedef unsigned long long ULL;

ULL P, Q;

int MinGenerations() {
  int level = 0, ans = 0;
  while (P < Q && P > 0 && level <= 40) {
    P *= 2;
    ++level;
    if (P >= Q) {
      P -= Q;
      if (!ans)
        ans = level;
    }
  }
  if (level <= 40)
    return ans;
  else
    return 0;
}

int main() {
  int T;
  stringstream ss;
  string pq;
  char tmp;
  cin >> T;
  for (int c = 1; c <= T; ++c) {
    ss.str(""); ss.clear();
    cin >> pq;
    ss << pq;
    ss >> P >> tmp >> Q;
    int g = MinGenerations();
    if (g)
      cout << "Case #" << c << ": " << g << endl;
    else
      cout << "Case #" << c << ": impossible" << endl;
  }
  return 0;
}
