#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define sMax 100

int main(void)
{
     int T;
     scanf("%d", &T);
     while(getchar() != '\n');

     for(int i=0; i<T; i++){
          char S[sMax+1] = {NULL};
          int sLen;
          scanf("%s", S);
          sLen = strlen(S);

          int flip = 0;
          for(int j=sLen-1; j >= 0; j--){
               if(S[j] == '+')
                    continue;
               flip++;
               for(int k=j; k >= 0; k--){
                    if(S[k] == '+')
                         S[k] = '-';
                    else
                         S[k] = '+';
               }
          }

          printf("Case #%d: %d\n", i+1, flip);
     }
}
