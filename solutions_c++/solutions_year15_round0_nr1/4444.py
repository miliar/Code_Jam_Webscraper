#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int S;
    cin >> S;
    int tot = 0;
    int needed = 0;
    for (int s = 0; s <= S; s++) {
      char c;
      cin >> c;
      int n = c - '0';
      tot += n;
      if (tot <= s) {
	needed++;
	tot++;
      }
    }
    cout << "Case #" << t << ": " << needed << endl;
  }
}
