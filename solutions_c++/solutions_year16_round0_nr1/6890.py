#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
     int num;
     int N = 1000000;
     scanf("%d", &num);

     for(int i=0; i<num; i++){
          int T;
          int max = 0;
          int a = 0;
          int aList[10] = {0};
          
          scanf("%d", &T);

          for (int j=1; j<N+1; j++){
              int t = T * j;
              if(max < t)
                   max = t;
              while(t != 0){
                   int tmp = t%10;
                   if(aList[tmp] == 0){
                         aList[tmp] = 1;
                         a++;
                   }
                   t /= 10;
              }
              if(a==10)
                   break;
          }

          if(a == 10)
               printf("Case #%d: %d\n", i+1, max);
          else
               printf("Case #%d: INSOMNIA\n", i+1);
     }
}
