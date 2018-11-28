#include <iostream>
#include <functional>
#include <vector>
#include <queue>
using namespace std;

int findBest(priority_queue<int, vector<int>, less<int> > pancakes, int best, int i, int specials) {
  if (i < 0) return best;
  int steps_i = pancakes.top(); pancakes.pop();
  int steps = steps_i + specials;
  best = min(best, steps);
  if (steps_i % 3 == 0) {
    int tmp = steps_i / 3;
    priority_queue<int, vector<int>, less<int> > pancakes2(pancakes);
    pancakes2.push(tmp);
    pancakes2.push(tmp);
    pancakes2.push(tmp);
    best = min(best, findBest(pancakes2, best, i - 1, specials + 2));
  }
  int tmp = steps_i / 2;
  pancakes.push(steps_i - tmp);
  pancakes.push(tmp);
  best = min(best, findBest(pancakes, best, i - 1, specials + 1));
  return best;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int diners, p;
    priority_queue<int, vector<int>, less<int> > pancakes;  // top == max
    cin >> diners;
    for (int i = 0; i < diners; i++) {
      cin >> p; pancakes.push(p);
    }
    cout << "Case #" << t << ": " << findBest(pancakes, pancakes.top(), pancakes.top(), 0) << endl;
  }
  return 0;
}