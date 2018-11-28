#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char str[10000];
char newstr[10000];

int main(int argc, char const *argv[]) {
  int n;
  scanf("%d\n", &n);
  for(int i=0;i<n;i++){
    scanf("%s\n", str);
    int len=strlen(str);
    char *start, *end;
    start = newstr+2000; end=newstr+2000; *(end+1)='\0';
    *start = str[0];
    for(int j=1;j<len;j++){
      if(str[j]>=*start){
        start--;
        *start=str[j];
      }else{
        end++;
        *end=str[j];
        *(end+1)='\0';
      }
    }
    printf("Case #%d: %s\n", i+1, start);
  }
  return 0;
}
