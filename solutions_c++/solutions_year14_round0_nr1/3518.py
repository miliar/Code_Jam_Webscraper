#include <stdio.h>
int final,a[4][4],b[4][4];
int intersection(int first, int second)
{   
    int count = 0, i,j;
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
               if (a[first-1][i] == b[second-1][j]) {
                   count++;
                   final = a[first-1][i];
               }
        }
    }
    return count;
                  
}
int main()
{
    int t, first, second,i,k,j,ans;
    scanf("%d",&t);
    for (k = 1; k <= t; k++) {
          scanf("%d",&first);
          for (i = 0; i < 4; i++) {
              for (j = 0; j < 4; j++) {
                  scanf("%d",&a[i][j]);
              }
          }
          scanf("%d",&second);
          for (i = 0; i < 4; i++) {
              for (j = 0; j < 4; j++) {
                  scanf("%d",&b[i][j]);
              }
          }
          
          ans = intersection(first,second);
          if (ans == 1) {
             printf("Case #%d: %d\n",k,final);
          }
          else if (ans == 0) {
               printf("Case #%d: Volunteer cheated!\n",k);
          }
          else if (ans > 1) {
               printf("Case #%d: Bad magician!\n",k);
          }
    }
    main();
    return 0;
    
}
