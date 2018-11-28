#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using std::cout;
using std::cin;
using std::set;
using std::vector;

void skip(int to_skip) {
  int dummy;
  for (int i = 0; i < to_skip; i++) {
    for (int j = 0; j < 4; j++) {
      cin >> dummy;
    }
  }
}

set<int> get_candidates() {
  set<int> candidates;
  int holder;
  int row;
  cin >> row;

  int to_skip = row - 1;
  skip(to_skip);

  for (int i = 0; i < 4; i++) {
    cin >> holder;
    candidates.insert(holder);
  }

  skip(4 - to_skip - 1);
  return candidates;
}

int main(int argc, char* argv[]) {
  int holder;
  int T = 0;
  cin >> T;
  for (int i = 0; i < T; i++) {
    set<int> candidates1 = get_candidates();
    set<int> candidates2 = get_candidates();
    vector<int> solns(4);

    auto it = set_intersection(candidates1.begin(), candidates1.end(), candidates2.begin(), candidates2.end(), solns.begin());
    solns.resize(it - solns.begin());

    cout << "Case #" << i+1 << ": ";
    if (solns.size() == 1)
      cout << solns[0] << "\n";
    else if (solns.size() == 0)
      cout << "Volunteer cheated!\n";
    else
      cout << "Bad magician!\n";
  }

  return 0;
}
