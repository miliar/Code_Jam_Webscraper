#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int t = 5, i = 0, j = 0, k = 0, end = 0, c = 0;
    char s[101];
   
    scanf("%d\n", &t);
    
    for(i = 0; i < t; i++) {
          fgets(s, 101, stdin);
          c = 0;
          do {
              for(j = strlen(s); j >= 0; j--){
                    
                    end = 1;
                    if(s[j] == '-') {
                            end = 0;
                            for(k = 0; k <= j; k++)
                                  s[k] = (s[k] == '+')? '-' : '+';
                            c++;
                            break;
                    }
              }
          }while(!end);
          printf("Case #%d: %d\n", i+1, c);    
    }
    return 0;
} 
