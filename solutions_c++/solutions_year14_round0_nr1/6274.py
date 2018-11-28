#include <stdio.h>
#include <string.h>

int a[20];
int b[20];

void mark(int arr[]) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int v;
            scanf("%d", &v);
            if (i == n-1) {
               arr[v] = 1;
            }
        }
    }
}

int main () {
    int kase;
    int h = 1;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          int n, m;
          memset(a,0,sizeof(a));
          memset(b,0,sizeof(b));
          mark(a);
          mark(b);
          int num = 0;
          int t = 0;
          for (int i = 1; i <= 16; ++i) {
              if (a[i] && b[i]) {
                 num++;
                 t = i;
              }
          }
          printf("Case #%d: ",h++);
          if (num == 0) {
             printf("Volunteer cheated!\n");
          }
          else if (num > 1) {
             printf("Bad magician!\n");
          }
          else {
               printf("%d\n",t);
          }
    } 
    return 0;
}
