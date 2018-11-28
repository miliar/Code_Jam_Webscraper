#include <cstdio>
#include <cstring>

int seenNumbers[10];
char tmp[1000000];

int main(){
  int t;
  int tcase = 1;
  scanf("%d", &t);
  while(t--){
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", tcase++);
    for(int i = 0; i < 10; i++)
        seenNumbers[i] = 0;
    if (n==0) {
      printf("INSOMNIA");
    } else {
      int m = n;
      int seen = 0;
      while(true){
        sprintf(tmp, "%d", n);
        int len = strlen(tmp);
        for(int i = 0; i < len; i++)
        {
          tmp[i] -= '0';
          if (seenNumbers[tmp[i]] == 0)
          {
            seenNumbers[tmp[i]] = 1;
            seen++;
          }
        }
        if (seen == 10){
          printf("%d", n);
          break;
        }
        n += m;
      }
    }
    printf("\n");
  }
  return 0;
}




