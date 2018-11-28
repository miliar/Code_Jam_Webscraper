#include <cstdio>
#include <algorithm>

using namespace std;
int T, row, i, j;
int mat[4][4], line[4];
int main() {
  scanf("%d", &T);
  for(int c=1; c<=T; c++) {
    scanf("%d", &row);
    for(i=0; i<4; i++)
      for(j=0; j<4; j++)
        scanf("%d", &mat[i][j]);
    for(i=0; i<4; i++)
      line[i] = mat[row-1][i];
    scanf("%d", &row);
    for(i=0; i<4; i++)
      for(j=0; j<4; j++)
        scanf("%d", &mat[i][j]);
    int ret = 0, ans;
    for(i=0; i<4; i++)
      for(j=0; j<4; j++)
        if(mat[row-1][j] == line[i]) {
          ret++;
          ans = line[i];
        }
    if(ret==0) printf("Case #%d: Volunteer cheated!\n", c);
    else if(ret>1) printf("Case #%d: Bad magician!\n", c);
    else printf("Case #%d: %d\n", c, ans);
  }
  return 0;
}
