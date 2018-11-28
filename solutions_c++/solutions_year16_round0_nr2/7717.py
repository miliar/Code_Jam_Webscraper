#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char p[1000];

int swap(int pos)
{
  if(pos == 0) {
    return 1;
  }
  
  char now = p[pos];
  --pos;
  while((pos >= 0) && (now == p[pos])) {
    --pos;
  }
  
  if(pos == -1) {
    return 1;
  }
   
  return 1 + swap(pos);
}

int main(int argc, char** argv)
{
  int nTest;
  scanf("%d", &nTest);
  
  for(int i = 1; i <= nTest; ++i) {
    unsigned count = 0;
    
    scanf("%s", p);
    int len = strlen(p);
    int pos = len - 1;
    
    if(p[pos]=='+') {
      count = swap(pos) - 1;
    }
    else {
      count = swap(pos);
    }
    
    printf("Case #%d: %u\n", i, count);
  }
  
  return 0;
}
