#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char str[10240];
int k;

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0 ; t < T; t++) {     
     scanf("%s %d", str, &k);
     int ret = 0;
     int sz = strlen(str);

     for (int i = 0; i < sz - k + 1; i ++) {
        if (str[i] == '-') {
           ret++;
           for (int j = 0; j < k; j++) {
              if (str[i + j] == '-') str[i + j] = '+';
              else if (str[i + j] == '+') str[i + j] = '-';
           }
        }
     }

     bool flag = true;
     for (int i = 0; i < sz; i ++) {
        if (str[i] == '-') {
           flag = false;
        }
     }
     if (!flag) printf("Case #%d: IMPOSSIBLE\n", t + 1);
     else printf("Case #%d: %d\n", t + 1, ret);
  }
}
