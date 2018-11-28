#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

bool flipped(string pancakes) {
  for (char current : pancakes) {
    if (current == '-') {
      return false;
    }
  }
  return true;
}

string flip_at(string pancakes, int position) {
  string portion_to_flip = pancakes.substr(0, position+1);
  string left_alone = pancakes.substr(position+1, pancakes.size());
  reverse(begin(portion_to_flip), end(portion_to_flip));
  for (int i = 0; i < portion_to_flip.length(); i++) {
    if (portion_to_flip[i] == '-') {
      portion_to_flip[i] = '+';
    } else {
      portion_to_flip[i] = '-';
    }
  }
  return portion_to_flip + left_alone;
}

bool dls(string pancakes, int limit, unordered_set<string> seen) {
  if (limit == 0) {
    return flipped(pancakes);
  }
  for (int i = 0; i < pancakes.length(); i++) {
    string flipped = flip_at(pancakes, i);
    if (seen.find(flipped) == end(seen)) {
      seen.emplace(flipped);
      if (dls(flipped, limit-1, seen)) {
        return true;
      }
    }
  }
  return false;
}

int solve(string pancakes) {
  int i = 0;
  while (true) {
    if (dls(pancakes, i, unordered_set<string>{})) {
      return i;
    }
    i++;
  }
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    string pancakes;
    cin >> pancakes;
    cout << "Case #" << i << ": " << solve(pancakes) << endl;
  }
}
