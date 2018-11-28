#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

int greedyWay(string pancakes, char aim) {
  if (pancakes.length() == 0) return 0;
  if (pancakes[pancakes.length() - 1] == aim) return greedyWay(pancakes.substr(0, pancakes.length() - 1), aim);
  return greedyWay(pancakes.substr(0, pancakes.length() - 1), aim == '+' ? '-' : '+') + 1;
}

int main() {
  int T;
  cin >> T;

  for (int kase = 1; kase <= T; kase++) {
    string str;
    cin >> str;

    cout << "Case #" << kase << ": " << greedyWay(str, '+') << endl;
  }

  return 0;
}
