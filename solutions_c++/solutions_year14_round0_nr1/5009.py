#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main () {
    int T;
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf ("%d", &T);
    for (int j = 1; j <= T; j++) {
          int ans[17] = {0};
          int tmp, q, flag = 0, target;
          scanf ("%d", &q);
          for (int i = 1; i <= 16; i++) {
              scanf ("%d", &tmp);
              if ((i-1) / 4 == (q-1))
                 ans[tmp]++;
          }
          scanf ("%d", &q);
          for (int i = 1; i <= 16; i++) {
              scanf ("%d", &tmp);
              if ((i-1) / 4 == (q-1))
                 ans[tmp]++;
          }
          for (int i = 1; i <= 16; i++)
              if (ans[i] == 2) {
                 flag++;
                 target = i;
                 if (flag > 1)
                    break;
              }
          if (flag == 0)
             printf ("Case #%d: Volunteer cheated!\n", j);
          if (flag == 1)
             printf ("Case #%d: %d\n", j, target);
          if (flag > 1)
              printf ("Case #%d: Bad magician!\n", j);
    }
    return 0;
}
