#include <stdio.h>

long n, i, v, j, t, k, p, y, b;
long c[5][5], arr[5];

int main(){
    freopen("A-small-attempt2.in", "r", stdin);
	freopen("magic.out", "w", stdout);
   scanf("%ld", &t);
   for(k=1; k<=t; k++){
      v=0;
      p=0;
      b=0;
      scanf("%ld", &n);
      for(i=0; i<4; i++)
         for(j=0; j<4; j++){
            scanf("%ld", &c[i][j]);
            if(i==n-1){
                arr[v]=c[i][j];
                v++;
            }
         }
      scanf("%ld", &n);
      for(i=0; i<4; i++)
         for(j=0; j<4; j++){
            scanf("%ld", &c[i][j]);
            if(i==n-1){
                for(y=0; y<4; y++)
                   if(c[i][j]==arr[y]){
                       p=j;
                       b++;
                   }
            }
         }
      if(b==1)
        printf("Case #%ld: %ld\n", k, c[n-1][p]);
      if(b>1)
        printf("Case #%ld: Bad magician!\n", k);
      if(b<1)
        printf("Case #%ld: Volunteer cheated!\n", k);


   }
}
