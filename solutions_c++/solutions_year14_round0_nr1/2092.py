#include <iostream>

using namespace std;

int main() {
  int T, row, answer[4], buffer, count, result;
  cin >> T;
  for (int i = 1; i<=T; i++) {
    cin >> row;
    for (int j = 1; j <= 4; j++) {
      for (int k = 0; k<4; k++) {
        if (j==row) {
          cin >> answer[k];
        } else {
          cin >> buffer;
        }  
      }
    }
    cin >> row;
    count = 0;
    for (int j=1; j<=4; j++) {
      for (int k = 0; k<4; k++) {
        cin >> buffer;
        if (j==row && (buffer == answer[0] ||buffer == answer[1]||buffer == answer[2]||buffer == answer[3])) {
          count++;
          result = buffer;
        }
      }
    }
    cout << "Case #" << i << ": ";
    if (count==1) {
      cout << result;
    } else if (count > 1) {
      cout << "Bad magician!";
    } else {
      cout << "Volunteer cheated!";
    }
    cout << endl;
  }
}