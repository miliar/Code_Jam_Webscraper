#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    string pancake;
    cin >> pancake;

    int count = 0;
    for (int i = 1; i < pancake.length(); ++i) {
      if (pancake[i] != pancake[i-1]) ++count;
    }
    if (count % 2 == 0 && pancake[0] == '-') ++count;
    if (count % 2 == 1 && pancake[0] == '+') ++count;
    cout << "Case #" << t << ": " << count << endl;
  }
  return 0;
}
