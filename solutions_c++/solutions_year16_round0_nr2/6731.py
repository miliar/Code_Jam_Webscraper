#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void generate_flips(string stack) {
  // Start from the back
  // Skip all the pluses first
  // Then, after that start flipping every time the sign changes

  char prev = '+';
  int length = stack.length();
  int flips = 0;

  for (int i = length - 1; i >= 0; i--) {
    if (stack[i] != prev) {
      prev = stack[i];
      flips++;
    }
  }

  cout << flips;
}

int main() {
  string line;

  int cases;
  cin >> cases;

  for (int i = 0; i < cases; i++) {
    string stack;
    cin >> stack;
    cout << "Case #" << (i + 1) << ": ";
    generate_flips(stack);
    cout << "\n";
  }
}
