#include <iostream>
#include <string>

using namespace std;

bool Ready(string& str, int n) {
  for (auto c : str)
    if (c == '-') {
      int i = 0;
      char pivot = str[0];
      char flip = pivot == '+' ? '-' : '+';

      while (i < n && str[i] == pivot) str[i++] = flip;

      return false;
    }

  return true;
}

int main() {

  int n;

  cin >> n;

  for (int games = 1; games <= n; games++) {
    cout << "Case #" << games << ": ";

    string str;

    cin >> str;

    int counter = 0;
    while (!Ready(str, str.size())) counter++;

    cout << counter << endl;
  }

  return 0;
}
