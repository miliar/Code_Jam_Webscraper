#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LEN 1000

char str[LEN];

int main(int argc, char const *argv[]) {
  int n;
  scanf("%d\n", &n);
  for(int i=0;i<n;i++){
    scanf("%s\n", str);
    int count=0;
    int len=strlen(str);
    for(int i=1;i<len;i++){
      if(str[i-1] != str[i])  count++;
    }
    if(str[len-1]=='-')  count++;
    printf("Case #%d: %d\n", i+1, count);
  }
  return 0;
}
