#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

int main() {
  int T;
  char str[1001];
  char result[3001];
  scanf("%d", &T);
  for (int cs=1; cs<=T; cs++){
    scanf("%s", str);
    int len = strlen(str);
    int first = 1500;
    int last = 1500;
    result[first] = str[0];
    for (int i=1;i<len;i++){
      if (str[i] >= result[first]) {
        first--;
        result[first]=str[i];
      }else{
        last++;
        result[last]=str[i];
      }
    }
    printf("Case #%d: ", cs);
    for (int i=first;i<=last;i++){
      printf("%c", result[i]);
    }
    printf("\n");
  }
  return 0;
}
