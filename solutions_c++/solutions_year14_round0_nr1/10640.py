#include<iostream>
#include <algorithm>
#include <vector>

#define COLS	4
#define ROWS	4

using namespace std;

void read_row(int* row) {
  int tmp[COLS];
  int row_no;
  cin >> row_no; cin.ignore(256, '\n');
  
  for (int i = 1; i < row_no; ++i) {
    cin.ignore(256, '\n');
  }
  
  for (int i = 0; i < COLS; ++i) {
    cin >> row[i];
  }
  cin.ignore(256, '\n');

  
  for (int i = row_no + 1; i <= ROWS; ++i ) {
    cin.ignore(256, '\n');
  }
}

int perform_trick() {
  int row_1[COLS], row_2[COLS];
  vector<int> v(4);
  vector<int>::iterator it;
  
  read_row(row_1);
  read_row(row_2);
  sort(row_1, row_1 + COLS);
  sort(row_2, row_2 + COLS);
  it = set_intersection(row_1, row_1 + COLS, row_2, row_2 + COLS, v.begin());
  v.resize(it - v.begin());
  
  switch(v.size()) {
    case 0: return -1;
    case 1: return v[0];
    default: return -2;
  }
}

int main() {
  int T;

  cin >> T;
  
  for (int i = 1; i <= T; ++i) {
    int answer = perform_trick();
    cout << "Case #" << i << ": ";
    switch (answer) {
      case -2: cout << "Bad magician!"; break;
      case -1: cout << "Volunteer cheated!"; break;
      default: cout << answer;
    }
    cout << "\n";
  }
  
  return 0;
}