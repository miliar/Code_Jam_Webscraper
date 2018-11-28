#include <iostream>
using namespace std;

int tn;
int a[4][4];
int ca, cb;
int b[4][4];
int main(int argc, char *argv[])
{
  cin >> tn;
  for (int ti = 1; ti <= tn; ++ti) {
    cin >> ca;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        cin >> a[i][j];
      }
    }
    cin >> cb;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        cin >> b[i][j];
      }
    }

    int cnt[17] = {0, };
    for (int i = 0; i < 4; ++i) {
      cnt[a[ca-1][i]] ++;
    }
    for (int i = 0; i < 4; ++i) {
      cnt[b[cb-1][i]] ++;
    }
    int choice = 0;
    for (int i = 1; i <= 16; ++i) {
      if (cnt[i] == 2) {
        if (choice != 0) {
          choice = -1;
          continue;
        }
        choice = i;
      }
    }
    if (choice == 0) {
      cout << "Case #" << ti << ": Volunteer cheated!" << endl;
    } else if (choice == -1) {
      cout << "Case #" << ti << ": Bad magician!" << endl;
    } else {
      cout << "Case #" << ti << ": " << choice << endl;
    }
  }
  return 0;
}
