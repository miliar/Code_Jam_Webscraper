#include <iostream>
#include <string>

using namespace std;

// O(n) solution where n is size of the stack
// Could use templates for more assurance
int numFlips(string stack) {
  int returnNum = 0, i = 0, j = 0; // return and counter variables
  char tmp; // tmp comparison character
  
  /**
   * Inchworm our tmp character through the stack and keep track
   * of the number of times a single segment of the string contains
   * characters opposite its neighbors. In short, keep track of how many
   * flips from the top of the stack going down, we'd have to make to get
   * all characters (pancakes) equal.
   * (Left = top, Right = bottom)
   *    --+++-+--
   * => +++++-+-- (1)
   * => ------+-- (2)
   * => +++++++-- (3)
   * => --------- (4)
   * => +++++++++ (5) done
   */
  while (i < stack.size()) {
    tmp = stack[i];
    j = i+1;

    // Keep moving index j toward end of 'stack' until we
    // 1.) Hit the end
    // 2.) stack[i] != stack[j]
    while (j < stack.size() && tmp == stack[j]) {
      j++;
    }

    // Move i all the way up to index j where we're either at the end
    // or characters at the two indices are not equal
    i = j;

    if (j < stack.size()) returnNum++;
  }

  // If we end on a '-' we have to flip the whole stack one more time to '+'
  if (tmp == '-') returnNum++;

  return returnNum;
}

int main() {
  int T;
  string line;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> line;
    cout << "Case #" << i+1 << ": " << numFlips(line) << endl;
  }

  return 0;
}