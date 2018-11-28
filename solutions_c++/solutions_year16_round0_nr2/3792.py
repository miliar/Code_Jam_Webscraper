#include <iostream>
#include <string>
#include <vector>

using namespace std;

int countChanges(string s) {
  char firstValue = s[0];
  char currentValue = firstValue;
  int changes = 0;
  for (int i = 1; i < s.length(); ++i) {
    char c = s[i];
    if (c != currentValue) {
      changes++;
      currentValue = c;
    }
  }
  if (currentValue == '-') changes++;
  return changes;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  int t = 0;
  for (int t = 1; t <= T; ++t) {
    string s;
    cin >> s;
    int steps = countChanges(s);
    cout << "Case #" << t << ": " << steps << endl;
  }
  return 0;
}