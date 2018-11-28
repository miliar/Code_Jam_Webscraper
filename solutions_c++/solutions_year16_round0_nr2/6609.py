#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char * argv []){
  int T;
  scanf("%d", &T);

  for(int i = 0; i < T; i++){
    char S[102];
    scanf("%s", S);
    int len = strlen(S);
    S[len] = '+';
    S[len + 1] = '\0';
    len++;
    int ANS = 0;
    for(int j = 1; j < len; j++){
      if(S[j] != S[j - 1]) ANS++;
    }
    printf("Case #%d: ", i + 1);
    printf("%d\n", ANS);
  }

  return 0;
}


