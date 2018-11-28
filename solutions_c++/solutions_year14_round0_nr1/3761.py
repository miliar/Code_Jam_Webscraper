#include <iostream>
#include <cstdio>
#include <unordered_set>
#include <vector>

using namespace std;

void guess(const vector<vector<int> > &arr1, int a1, const vector<vector<int> > &arr2, int a2) {
  unordered_set<int> memo;
  for (int i = 0; i < 4; ++i) {
    memo.insert(arr1[a1-1][i]);
  }

  int res = 0;

  for (int i = 0; i < 4; ++i) {
    if (memo.count(arr2[a2-1][i])) {
      if (res != 0) {
        cout << "Bad magician!" << endl;
        return;
      } else {
        res = arr2[a2-1][i];
      }
    }
  }
  
  if (res == 0) {
    cout << "Volunteer cheated!" << endl;
  } else {
    cout << res << endl;
  }

}

int main() {
  int T;
  cin >> T;
  vector<vector<int> > arr1(4, vector<int>(4));
  vector<vector<int> > arr2(4, vector<int>(4));
  int a1, a2;

  for (int i = 1; i <= T; ++i) {
    cin >> a1;
    for (int i = 0; i < 4; ++i) {
      cin >> arr1[i][0] >> arr1[i][1] >> arr1[i][2] >> arr1[i][3];
    }
    cin >> a2;
    for (int i = 0; i < 4; ++i) {
      cin >> arr2[i][0] >> arr2[i][1] >> arr2[i][2] >> arr2[i][3];
    }
    printf("Case #%d: ", i);
    guess(arr1, a1, arr2, a2);
  }

  return 0;
}
