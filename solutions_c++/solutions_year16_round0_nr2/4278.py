/* The inputs are small, I think we should brute force this.
  Although, you wouldn't want to bother attempting every situation.

  --+-

  Pick up top two, flip. Pick up top three, flip. Pick up all, flip.
  What if we attempt flipping at each change in which side is up.

  Flip --+ to give -++-. But you don't want to repeat states, so you wouldn't
  want to flip to get --+- again.
  So I guess you could store which ones. Connie would be happy, it's a DP
  problem.
*/
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <string>
using namespace std;

// Takes the pancakes upto and including bottom
string flip_at_point(string stack, int bottom) {
  string new_stack;
  for (int i = bottom; i >= 0; i--) {
    if (stack[i] == '+') {
      new_stack += '-';
    } else {
      new_stack += '+';
    }
  }

  new_stack += stack.substr(bottom + 1);

  return new_stack;
}

// flips_til_happiness[x] = -1 indicates that x is still being processed and we
// shouldn't go back to it.
map<string, int> flips_til_happiness;

int how_many_flips(string stack) {
  // cout << "how many flips? " << stack << endl;
  // Dynamic programming optimisation
  if (flips_til_happiness.count(stack) != 0) {
    // cout << "calculated before: " << flips_til_happiness[stack] << endl;
    return flips_til_happiness[stack];
  }

  flips_til_happiness[stack] = -1;

  // Base cases: all pancakes are the right side up, or none are

  bool all_up = true;
  bool all_down = true;

  for (auto pancake : stack) {
    all_down = all_down && (pancake == '-');
    all_up = all_up && (pancake == '+');
  }

  if (all_up) {
    // cout << stack << " is all ready" << endl; 
    flips_til_happiness[stack] = 0;
    return 0;
  }

  if (all_down) {
    // cout << stack << " is nearly ready" << endl;
    flips_til_happiness[stack] = 1;
    return 1;
  }

  // Recursive case: flip where the direction of the pancakes change.

  int min_flips = INT_MAX;
  for (int i = 0; i < stack.length() - 1; i++) {
    if (stack[i] != stack[i+1]) {
      string flipped = flip_at_point(stack, i);
      // Don't flip ones that are in progress, because that turns your search
      // tree into a cylic graph.
      if (!flips_til_happiness.count(flipped) || flips_til_happiness[flipped] != -1) {
        // cout << "flipping " << stack << " to give " << flipped << endl;
        min_flips = 1 + how_many_flips(flipped);
        break;
      }
    }
  }

  // cout << "flips_til_happiness[" << stack << "] = " << min_flips << endl;
  flips_til_happiness[stack] = min_flips;
  return min_flips;
}

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string S;
    cin >> S;
    cout << "Case #" << t << ": " << how_many_flips(S) << endl;
  }

  return 0;
}
