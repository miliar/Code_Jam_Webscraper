#include <iostream>
using namespace std;

int main() {
  int t, state, step;
  bool lastState;
  string n;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n;
    state = -1;
    step = 0;
    lastState = (n[0] == '-') ? true : false;
    for (size_t j = 0; j < n.size(); j++) {
      if ((n[j] == '-' && lastState == true) || (n[j] == '+' && lastState == false) || state == -1) {
        lastState = !lastState;
        state = 1;
        step += 1;
      }
    }
    if (n[n.size() - 1] == '+' && step > 0)
      step -= 1;
    cout << "Case #" << i << ": " << step << endl;
  }
  return (0);
}
