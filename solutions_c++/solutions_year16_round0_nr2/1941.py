#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

uint64_t solve(vector<bool>& happy, uint64_t acc) {
  int firstChange = 0;

  assert(happy.size() > 0);
  const bool first = happy[0];
  for (int i = 0; i < happy.size(); ++i) {
    if (happy[i] != first) {
      firstChange = i;
      break;
    }
  } 
  if (firstChange == 0) {
    if (!first) {
      return acc + 1;
    }
    else {
      return acc;
    }
  }

  // otherwise, flip up to (not including) firstChange
  for (int j = 0; j < firstChange; ++j) {
    happy[j] = !happy[j];
  }

  return solve(happy, acc+1);
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  string _s;
  getline(cin, _s); // unused

  for (int t = 1; t <= T; ++t) {
    string state;
    getline(cin, state);
    vector<bool> happy;
    for (const char c : state) {
      if (c == '-') {
        happy.push_back(false);
      } else if (c == '+') {
        happy.push_back(true);
      } else {
        throw std::runtime_error("wtf");
      }
    }

    //for (const auto b : happy) {
    //  cout << b;
    //}
    //cout << endl;

    cout << "Case #" << t << ": "
         << solve(happy, 0) << '\n';
  }

  return 0;
}
