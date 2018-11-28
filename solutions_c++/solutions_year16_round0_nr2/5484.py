#include <cstdio>
#include <cstring>
char s[101];
int main(){
  int t,sum;
  scanf("%d", &t);
  for(int i = 0; i < t; i++){
    scanf("%s",s);
    sum = 0;
    for(int j = 0; j < strlen(s)-1; j++){
      if(s[j] != s[j+1]){
        sum++;
      }
    }
    if(s[strlen(s)-1] == '-')
      sum++;
    printf("Case #%d: %d\n", i+1, sum);
  }
}
