#include <iostream>
#include <vector>
#include <list>

using namespace std;

void testtestI(int testI) {
  int answer1, answer2;
  int matrix1[4][4];
  int matrix2[4][4];

  cin >> answer1; --answer1;

  for (int r = 0; r < 4; ++r) {
    for (int c = 0; c < 4; ++c) {
      cin >> matrix1[r][c];
    }
  }

  cin >> answer2; --answer2;

  for (int r = 0; r < 4; ++r) {
    for (int c = 0; c < 4; ++c) {
      cin >> matrix2[r][c];
    }
  }

  int matches = 0;
  int lastMatch = 0;
  for (int c1 = 0; c1 < 4; ++c1) {
    for (int c2 = 0; c2 < 4; ++c2) {
      if (matrix1[answer1][c1] == matrix2[answer2][c2]) {
        lastMatch = matrix1[answer1][c1];
        ++matches;
      }
    }
  }

  if (matches == 0) {
    cout << "Case #" << testI << ": Volunteer cheated!" << endl;
  } else if (matches == 1) {
    cout << "Case #" << testI << ": " << lastMatch << endl;
  } else {
    cout << "Case #" << testI << ": Bad magician!" << endl;
  }
}

int main(void) {
  ios_base::sync_with_stdio(false);
  
  int testN; cin >> testN;
  for (int testI = 1; testI <= testN; ++testI) {
    testtestI(testI);
  }

  return 0;
}
