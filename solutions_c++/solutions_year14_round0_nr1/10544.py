#include <stdio.h>
#include <stdlib.h>

int last;
int grid1[4][4], grid2[4][4];

int compare(int * a, int * b) {
  int count = 0;
  for(int i=0; i<4; ++i)
    for(int j=0; j<4; ++j) 
      if(a[i]==b[j]) {
        count++;
        last = a[i];
      }
  return count;
}

int main() {
  int T; scanf("%d", &T);
  for(int ic=1; ic<=T; ++ic) {
    printf("Case #%d: ", ic);
    int ch1, ch2; 
    scanf("%d", &ch1);
    for(int i=0; i<4; ++i) for(int j=0; j<4; ++j) scanf("%d", &grid1[i][j]);
    scanf("%d", &ch2);
    for(int i=0; i<4; ++i) for(int j=0; j<4; ++j) scanf("%d", &grid2[i][j]);
    int result = compare(grid1[ch1-1], grid2[ch2-1]);
    if(result == 0) {
      printf("Volunteer cheated!\n");
    } else if(result == 1) {
      printf("%d\n", last);    
    } else {
      printf("Bad magician!\n");
    }
  }
  return 0;
}
