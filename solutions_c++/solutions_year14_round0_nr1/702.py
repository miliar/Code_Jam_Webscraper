// mars.ma
#include <iostream>
#include <vector>
#include <set>

using namespace std;
const int SIDE = 4;

int main(void)
{
  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    int answer;
    set<int> numbers;
    cin >> answer;
    for (int row = 0; row < SIDE; ++row) {
      for (int col = 0; col < SIDE; ++col) {
        int num;  cin >> num;
        if (row+1 == answer) {
          numbers.insert(num);
        }
      }
    }

    set<int> overlap;
    cin >> answer;
    for (int row = 0; row < SIDE; ++row) {
      for (int col = 0; col < SIDE; ++col) {
        int num;  cin >> num;
        if (row+1 == answer) {
          if (numbers.end() != numbers.find(num)) {
            overlap.insert(num);
          }
        }
      }
    }

    cout << "Case #" << tc << ": ";
    if (0 == overlap.size()) {
      cout << "Volunteer cheated!\n";
    } else if (1 == overlap.size()) {
      cout << *overlap.begin() << endl;
    } else {
      cout << "Bad magician!\n";
    }
  }

  return 0;
}

