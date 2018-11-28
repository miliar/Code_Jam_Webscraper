#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int a, b, am[4][4], bm[4][4];
    cin >> a;
    for (int j = 0; j < 4; j++)
      for (int k = 0; k < 4; k++)
	cin >> am[j][k];
    cin >> b;
    for (int j = 0; j < 4; j++)
      for (int k = 0; k < 4; k++)
	cin >> bm[j][k];
    int same = 0, same_num; 
    for (int j = 0; j < 4; j++)
      for (int k = 0; k < 4; k++)
	if (am[a-1][j] == bm[b-1][k]) {
	  same++;
	  same_num = am[a-1][j];
	}
    switch (same) {
    case 0:
      printf("Case #%d: Volunteer cheated!\n", i+1);
      break;
    case 1:
      printf("Case #%d: %d\n", i+1, same_num);
      break;
    default:
      printf("Case #%d: Bad magician!\n", i+1);
      break;
    }
  }
}
