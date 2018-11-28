
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <sstream>

#include <algorithm>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <vector>

using namespace std;

int main(int argc, const char *argv[]) {

  int num_cases;
  cin >> num_cases;

  for (int i = 1; i <= num_cases; ++i) {

    set<int> set1;
    set<int> set2;
    string temp;

    int row1;
    cin >> row1;
    getline(cin, temp);
    for (int i = 1; i < row1; ++i) {
      getline(cin, temp);
    }

    for (int i = 0; i < 4; ++i) {
      int num;
      cin >> num;
      set1.insert(num);
    }
    getline(cin, temp);

    for (int i = row1 + 1; i <= 4; ++i) {
      getline(cin, temp);
    }

    int row2;
    cin >> row2;
    getline(cin, temp);
    for (int i = 1; i < row2; ++i) {
      string temp;
      getline(cin, temp);
    }

    for (int i = 0; i < 4; ++i) {
      int num;
      cin >> num;
      set2.insert(num);
    }
    getline(cin, temp);

    for (int i = row2 + 1; i <= 4; ++i) {
      string temp;
      getline(cin, temp);
    }

    set<int> intersection;
    set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                     inserter(intersection, intersection.end()));
    if (intersection.size() == 0)
      cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
    else if (intersection.size() > 1)
      cout << "Case #" << i << ": " << "Bad magician!" << endl;
    else
      cout << "Case #" << i << ": " << *(intersection.begin()) << endl;
  }

  return 0;
}

