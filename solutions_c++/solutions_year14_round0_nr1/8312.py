#include <cstdio>
#include <cstring>


int check[20];

int main() {
  int t,a,b;
  int tmp;
  scanf("%d", &t);
  for ( int tc = 1; tc<=t; tc++ ){
    printf("Case #%d: ", tc);
    memset(check, 0, sizeof(check));

    scanf("%d", &a);
    for (int i = 1; i<=4; i++)
      for (int j = 0; j<4; j++) {
        scanf("%d", &tmp);
        if ( i == a ) {
          check[tmp] = 1;
        }
      }
    scanf("%d", &b);
    for (int i = 1; i<=4; i++)
      for (int j = 0; j<4; j++) {
        scanf("%d", &tmp);
        if ( i == b )
          check[tmp]++;
       }
    int y = -1;
    int cnt = 0;
    for ( int i = 1; i<=16; i++ ){
      if ( check[i] == 2 ){
        y = i;
        cnt++;
      }
    }
    if( cnt == 1 ){
      printf("%d\n", y);
      continue;
    } 
    if( cnt == 0 ){
      printf("Volunteer cheated!\n");
      continue;
    } 
    printf("Bad magician!\n");
  } 
  return 0;
}
