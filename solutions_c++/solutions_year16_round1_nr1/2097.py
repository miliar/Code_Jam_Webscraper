#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solver {
 public:
  void Solve() {
    string output = "";
    output += input[0];
    for (int i = 1; i < input.size(); ++i) {
      if (output[0] <= input[i]) output = input[i] + output;
      else output = output + input[i];
    }
    cout << output << endl;
  }

  string input;
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    Solver solver;
    cout << "Case #" << t + 1 << ": ";
    cin >> solver.input;
    solver.Solve();
  }
}
