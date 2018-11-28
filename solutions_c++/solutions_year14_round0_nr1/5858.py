#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int i, j, k, T, tc, a1, a2;

int main()
{
  int label;

  cin >> T;
  
  for (tc = 0; tc < T; tc++) {
    vector<int> commons;
    vector< vector<int> > firstArr, secondArr;
    cin >> a1;
    for (i = 0; i < 4; i++) {
      vector<int> row;
      for (j = 0; j < 4; j++) {
        cin >> label;
        row.push_back(label);
      }
      firstArr.push_back(row);
    }
    cin >> a2;
    for (i = 0; i < 4; i++) {
      vector<int> row;
      for (j = 0; j < 4; j++) {
        cin >> label;
        row.push_back(label);
      }
      secondArr.push_back(row);
    }

    a1--;
    a2--;

    for (i = 0; i < 4; i++) {
      for (j = 0; j < 4; j++) {
        if(firstArr[a1][i] == secondArr[a2][j]) {
          commons.push_back(firstArr[a1][i]);
        }
      }
    }
    if(commons.size() == 1) {
      cout << "Case #" << (tc+1) << ": " << commons[0] << endl;
    }
    else if(commons.size() > 1) {
      cout << "Case #" << (tc+1) << ": Bad magician!" << endl;
    }
    else {
      cout << "Case #" << (tc+1) << ": Volunteer cheated!" << endl;
    }
  }

  return 0;
}
