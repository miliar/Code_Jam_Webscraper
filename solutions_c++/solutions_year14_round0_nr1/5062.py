#include <stdio.h>

int main()
{
    int t;
    int i;
    int j;
    int k;
    int n1;
    int n2;
    int a[5][5];
    int b[5][5];
    int c = 1;
    int ans;
    
    scanf("%d", &t);
    while(t--) {
               scanf("%d", &n1);
               for(i=1; i<=4; i++) {
                        for(j=1; j<=4; j++) {
                                 scanf("%d", &a[i][j]);
                        }
               }
               scanf("%d", &n2);
               for(i=1; i<=4; i++) {
                        for(j=1; j<=4; j++) {
                                 scanf("%d", &b[i][j]);
                        }
               }
               k = 0;
               for(i=1; i<=4; i++) {
                        for(j=1; j<=4; j++) {
                                 if(a[n1][i] == b[n2][j]) {
                                             k++;
                                             ans = a[n1][i];
                                 }
                        }
               }
               printf("Case #%d: ", c);
               if(k==1) {
                        printf("%d\n", ans);
               } else if(k>1) {
                      printf("Bad magician!\n");
               } else if(k==0) {
                      printf("Volunteer cheated!\n");
               }
               c++;
    }
    //main();
    return 0;
}
               
    
