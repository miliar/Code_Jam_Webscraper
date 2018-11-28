#include <cstdio>

int main(){
  int r1, c1[4][4], r2, c2[4][4];
  int ok[4], okct;
  for(int TT, T = (scanf("%d", &TT), 1); T <= TT; T++){
    printf("Case #%d: ", T);
    scanf("%d", &r1); r1--;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        scanf("%d", c1[i] + j);
    scanf("%d", &r2); r2--;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        scanf("%d", c2[i] + j);
    okct = 0;
    for(int j1 = 0; j1 < 4; j1++)
      for(int j2 = 0; j2 < 4; j2++){
        if(c1[r1][j1] == c2[r2][j2]){
          ok[okct++] = c1[r1][j1];
        }
      }
    if(okct > 1) printf("Bad magician!\n");
    else if(okct == 1) printf("%d\n", ok[0]);
    else printf("Volunteer cheated!\n");
  }
  return 0;
}
