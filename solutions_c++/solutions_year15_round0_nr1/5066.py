#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(string shy) {
  int add = 0;
  int result = 0;
  int standing = 0;
  for (int level=0; level<int(shy.length()); level++) {
    if (standing < level) {
      add=level-standing;
      standing += add;
      result += add;
    }
    standing += shy[level]-'0';
  }
  return result;
}

int main() {
  vector<int> result;

  int T;
  string shy;
  int s_max;
  cin >> T;

  for (int t=0; t<T; t++) {
    cin >> s_max >> shy;
    result.push_back(solve(shy));
  }

  for (int i=0; i<int(result.size()); i++) {
    cout << "Case #" << i+1 << ": " << result[i] << "\n";
  }
  return 0;
}
