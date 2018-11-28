#include <iostream>
using namespace std;

void swap(char &goal) {
  goal = goal == '+' ? '-' : '+';
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string stack;
    cin >> stack;
    char goal = '+';
    int flips = 0;
    for (int last = stack.size(); last > 0; last--) {
      if (stack[last-1] != goal) {
        flips++;
        swap(goal);
      }
    }
    cout << "Case #" << i << ": " << flips << endl;
  }
  return 0;
}
