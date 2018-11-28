#include <bits/stdc++.h>

using namespace std;

void solveTest() {
  int n;
  cin >> n;
  std::set<char> s;
  int x = 0;
  int iterCount = 0;
  while (s.size() < 10 && iterCount < 100) {
    x = x + n;
    auto st = to_string(x);
    s.insert(st.begin(), st.end());
    iterCount++;
  }
  if (iterCount >= 100) {
    cout << "INSOMNIA\n";
  } else {
    cout << x << "\n";
  }
}

int main() {
  int tn;
  cin >> tn;
  for (int tc = 0; tc < tn; tc++) {
    cout << "Case #" << (tc + 1) << ": ";
    solveTest();
  }
  return 0;
}
