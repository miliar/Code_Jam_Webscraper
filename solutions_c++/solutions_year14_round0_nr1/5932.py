#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> read_set() {
  int row_num;
  vector<vector<int>> nums;
  
  cin >> row_num;

  for (int i = 0; i < 4; i++) {
    vector<int> row;
    for (int j = 0; j < 4; j++) {
      int num;
      cin >> num;

      row.push_back(num);
    }
    nums.push_back(row);
  }

  return nums[row_num - 1];
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  for (int case_num = 1; case_num <= T; case_num++) {
    vector<int> set_one = read_set();
    vector<int> set_two = read_set();

    sort(set_one.begin(), set_one.end());
    sort(set_two.begin(), set_two.end());

    vector<int> intersection(4);
    vector<int>::iterator it = set_intersection(set_one.begin(), set_one.end(), set_two.begin(), set_two.end(), intersection.begin());
    intersection.resize(it - intersection.begin());

    cout << "Case #" << case_num << ": ";
    if (intersection.size() == 1) {
      cout << intersection[0] << endl;
    } else if (intersection.size() == 0) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }

  return 0;
}
