#include <iostream>
#include <cstring>

using namespace std;

void init() {
  // TODO
}

void solve_case(int t) {
  init();

  int arrange1[16];
  int arrange2[16];
  int row1, row2;

  cin >> row1; row1--;
  for (int i = 0; i < 16; i++)
    cin >> arrange1[i];

  cin >> row2; row2--;
  for (int i = 0; i < 16; i++)
    cin >> arrange2[i];

  int counts[16];
  memset(counts, 0, sizeof(counts));
  for (int i = 0; i < 4; i++) {
    counts[arrange1[4 * row1 + i] - 1]++;
  }
  for (int i = 0; i < 4; i++) {
    counts[arrange2[4 * row2 + i] - 1]++;
  }

  int answer = -1;
  for (int i = 0; i < 16; i++) {
    if (counts[i] == 2) {
      if (answer != -1) {
        answer = -2;
        break;
      }
      answer = i;
    }
  }

  if (answer == -1)
    cout << "Case #" << t << ": " << "Volunteer cheated!\n";
  else if (answer == -2)
    cout << "Case #" << t << ": " << "Bad magician!\n";
  else
    cout << "Case #" << t << ": " << (answer + 1) << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
