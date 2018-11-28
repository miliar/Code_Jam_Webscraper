#include <cstdio>
#include <vector>

using namespace std;

int main(void) {
  int t;
  int case_cnt = 1;
  scanf("%d", &t);
  while (t--) {
    vector <bool> possible(17, true);
    int row;
    for (int k = 0; k < 2; k++) {
      scanf("%d", &row);
      for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
          int x;
          scanf("%d", &x);
          if (i != row) possible[x] = false;
        }
      }
    }
    int cnt = 0;
    int last = 0;
    for (int i = 1; i <= 16; i++) {
      if (possible[i]) {
        cnt++;
        last = i;
      }
    }
    if (cnt == 0) {
      printf("Case #%d: Volunteer cheated!\n", case_cnt++);
    } else if (cnt == 1) {
      printf("Case #%d: %d\n", case_cnt++, last);
    } else {
      printf("Case #%d: Bad magician!\n", case_cnt++);
    }
  }
  return 0;
}

