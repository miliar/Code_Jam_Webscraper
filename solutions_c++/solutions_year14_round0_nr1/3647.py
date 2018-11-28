#include <iostream>
#include <set>

using namespace std;

set<int> readrow(int row) {
  set<int> result;
  for (int r = 0; r < 4; ++r) {
    for (int c = 0; c < 4; ++c) {
      int num;
      cin >> num;
      if (row == r + 1) {
        result.insert(num);
      }
    }
  }
  return result;
}

int main() {
  int ncases;
  cin >> ncases;
  
  for (int c = 0; c < ncases; ++c) {
    cout << "Case #" << c + 1 << ": ";
    int chosen1;
    cin >> chosen1;
    set<int> row1 = readrow(chosen1);
    int chosen2;
    cin >> chosen2;
    set<int> row2 = readrow(chosen2);
    int found = 0;
    int result;
    for (set<int>::iterator it = row1.begin(); it != row1.end(); ++it) {
      if (row2.count(*it) > 0) {
        ++found;
        result = *it;
      } 
    }
    if (1 == found) {
      cout << result << endl;
    } else if (0 == found) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}
