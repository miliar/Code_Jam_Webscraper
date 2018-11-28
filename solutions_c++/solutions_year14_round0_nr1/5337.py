#include <stdio.h>

int T;
int R;
int a[4][4];
int i, j;
int m[17];

int main() {

  scanf("%d", &T);
  int c = 0;
  while (T--) {
    c++;
    scanf("%d", &R);
    for (i = 0; i < 4; i++)
      for (j = 0; j < 4; j++)
	scanf("%d", &a[i][j]);
      
    for (i = 0; i < 17; i++) m[i] = 0;
    
    R--;
    for (j = 0; j < 4; j++) m[a[R][j]]++;

    scanf("%d", &R);
    for (i = 0; i < 4; i++)
      for (j = 0; j < 4; j++)
	scanf("%d", &a[i][j]);

    R--;
    for (j = 0; j < 4; j++) m[a[R][j]]++;
    
    int cnt = 0;
    int sol = 0;
    for (i = 1; i <= 16; i++)
      if (m[i] == 2) {
	cnt++;
	sol = i;
      }
    
    printf("Case #%d: ", c);
    
    if (cnt > 1) printf("Bad magician!\n");      
    if (cnt == 1) printf("%d\n", sol);      
    if (cnt == 0) printf("Volunteer cheated!\n");      
    
  }
  
  return 0;
}