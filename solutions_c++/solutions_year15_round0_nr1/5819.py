#include <iostream>
#include <string>
#include <vector>

using std::cin; using std::cout;
using std::string; using std::endl;
using std::vector;

typedef string::size_type str_sz;
typedef vector<int>::size_type vec_sz;

void processTestCase(int caseNumber, const string &line) {
  str_sz clapping = 0;
  str_sz friends = 0;
  for (str_sz i = 0; i < line.size(); i++) {
    int si = line[i] - '0';
    int moreFriends = 0;
    if (clapping < i) {
      moreFriends = i - clapping;
      friends += moreFriends;
    }
    clapping += moreFriends + si;
  }
  cout << "Case #" << caseNumber << ": " << friends << endl;
}

int main() {
  int t, sMax;
  string line;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> sMax;
    cin >> line;
    processTestCase(i + 1, line);
  }
  return 0;
}
