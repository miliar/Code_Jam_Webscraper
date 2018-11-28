#include <cstdio>
#include <cstdlib>
#include <algorithm>

int arr1[5][5];
int arr2[5][5];

void docase(int tcase)
{
  int r1; scanf("%d", &r1);
  for (int i = 1; i <= 4; i++)
    for (int j = 1; j <= 4; j++)
      scanf("%d", &arr1[i][j]);

  int r2; scanf("%d", &r2);
  for (int i = 1; i <= 4; i++)
    for (int j = 1; j <= 4; j++)
      scanf("%d", &arr2[i][j]);
  
  int table[20] = { 0 };
  for (int i = 1; i <= 4; i++) {
    table[arr1[r1][i]]++;
    table[arr2[r2][i]]++;
  }

  int count = 0, last = 0;
  for (int i = 1; i <= 16; i++)
  {
    if (table[i] == 2) {
      count++;
      last = i;
    }
  }

  if (count == 0)
    printf("Case #%d: Volunteer cheated!\n", tcase);
  else if (count == 1)
    printf("Case #%d: %d\n", tcase, last);
  else
    printf("Case #%d: Bad magician!\n", tcase);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; i++) docase(i+1);
}
