#include <iostream>
using namespace std;

int main() {
  int t;
  std::string line;

  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> line;
    int nb = 0;

    for (int j = 0; j + 1 < line.length(); j++) {
      if (line[j] != line[j + 1]) nb++;
    }

    if (line[line.length() - 1] == '-') nb++;
    cout << "Case #" << i << ": " << nb << endl;
  }
  return 0;
}
