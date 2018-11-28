#include <stdio.h>
#include <stdlib.h>

int main() {
    int t = 0, i = 0, j = 0;
    unsigned long long int n = 0, o_n;
    int a[10] = {0};
    int end = 0, c = 0;
    double temp = 0;
    scanf("%d", &t);
    
    for(i = 0; i < t; i++) {
          scanf("%u", &n);
          o_n = n;
          for(j = 0; j < 10; j++)
                a[j] = 0;
          c = 0;
          end = 0;
          
          if(n == 0) {
               printf("Case #%d: INSOMNIA\n", i+1);
          }
          else { 
              do {
                 temp = n;
                 n = (c+1) * o_n;
                 c++;
                 do{
                    a[((int)temp % 10)] = 1;
                    temp /= 10;
                 } while(temp>=1);
                 
                 end = 1;
                 for(j = 0; j < 10; j++) {
                         if (a[j] == 0)
                            end = 0;
                 }
              }while(!end);
              printf("Case #%d: %u\n", i+1, n - o_n);
          }
    }
    
    return 0;
} 
