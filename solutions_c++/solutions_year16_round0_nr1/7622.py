#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int src[1024];
bool dig[10];

int main(int argc, char** argv)
{
  int nTest;
  char buf[1024];
  
  
  scanf("%d", &nTest);
  for(int i = 1; i <= nTest; ++i) {
    memset(dig, false, sizeof(dig));
    int digCount = 0;
    
    scanf("%s", buf);
    int len = strlen(buf);
    if(len == 1 && buf[0] == '0' ) {
      printf("Case #%d: INSOMNIA\n", i);
      continue;
    }
    
    int olen = len;
    
    for(int j = 1; j <= 1000; ++j) {
      memset(src, 0, sizeof(src));
      int c = 0;
      for(int l = olen -1; l >= 0; --l, ++c) {      
        src[c] = (int)(buf[l] - '0');
      }      
      
      for(int l = 0; l < len; ++l) {
        src[l] = src[l] * j;
      }
      
      for(int l = 0; l < len; ++l) {
        if(src[l] > 9) {
          src[l+1]+=(src[l]/10);
          src[l]%=10;
          if((l+1) == len) {
            ++len;
          }
        }
      }

/*      
      printf("*%d = ", j);
      for(int j = len -1; j>=0; --j) {
        printf("%d ", src[j]);
      }
      printf("\n");
*/      
      for(int l = 0; l < len; ++l) {
        if(dig[src[l]] == false) {
          dig[src[l]] = true;
          ++digCount;
        }
      }
      
      if(digCount == 10) {
        break;
      }
    }
   
    printf("Case #%d: ", i);
    //if(digCount != 10) {
    //  printf("INSOMNIA");
    //}
    //else {
      for(int j = len -1; j>=0; --j) {
        printf("%d", src[j]);
      }
    //}
    printf("\n");
  }
  
  return 0;
}
