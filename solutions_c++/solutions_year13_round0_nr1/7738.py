#include <cstdio>
#include <cstdlib>
#include <string.h>
using namespace std;
int main() {
       int t, i, l, m, j=1, X=0, O=0, s[10], s1[10];
       char a[10][10];
       freopen("A-large.in", "r", stdin);
       freopen("A-large.out", "w", stdout);
       scanf("%d", &t);
       while(t--) {
                  for(i=0; i < 4; i++) for(l=0; l < 4; l++) {
                           scanf("%c", &a[i][l]);
                           if(a[i][l] == ' ' || a[i][l] == '\n') l--;
                  }
                  for(i=0; i < 4; i++) {
                           s[0]=0; s[1] = 0; s[2] = 0; s1[0]=0; s1[1] = 0; s1[2] = 0;
                           for(l=0; l < 4; l++) {
                                    if(a[i][l] == 'X') s[0]++;
                                    if(a[i][l] == 'O') s[1]++;
                                    if(a[i][l] == 'T') s[2]++;
                                    if(a[l][i] == 'X') s1[0]++;
                                    if(a[l][i] == 'O') s1[1]++;
                                    if(a[l][i] == 'T') s1[2]++;
                           }
                           if(s[0] == 4) X++;
                           if(s[1] == 4) O++;
                           if(s1[0] == 4)X++;
                           if(s1[1] == 4)O++;
                           if(s[0] == 3 && s[2] == 1) X++; 
                           if(s[1] == 3 && s[2] == 1) O++;
                           if(s1[0] == 3 && s1[2] == 1)X++;
                           if(s1[1] == 3 && s1[2] == 1)O++;
                  }
                  s[0]=0; s[1] = 0; s[2] = 0;
                  for(i=0, l=0; i < 4; i++, l++) {
                            if(a[i][l] == 'X') s[0]++;
                            if(a[i][l] == 'O') s[1]++;
                            if(a[i][l] == 'T') s[2]++;
                  }
                  if(s[0] == 4) X++;
                  if(s[1] == 4) O++;
                  if(s[0] == 3 && s[2] == 1) X++;
                  if(s[1] == 3 && s[2] == 1) O++;
                  s[0]=0; s[1] = 0; s[2] = 0;
                  for(i=3, l=0; i >= 0; i--, l++) {
                            if(a[i][l] == 'X') s[0]++;
                            if(a[i][l] == 'O') s[1]++;
                            if(a[i][l] == 'T') s[2]++;
                  }
                  if(s[0] == 4) X++;
                  if(s[1] == 4) O++;
                  if(s[0] == 3 && s[2] == 1) X++;
                  if(s[1] == 3 && s[2] == 1) O++;
                  if(X == 0 && O == 0) {
                       for(i=0; i < 4; i++) {
                                for(l=0; l < 4; l++) if(a[i][l] == '.') break;
                                if(l != 4) break;
                       }
                       if(i != 4) printf("Case #%d: Game has not completed\n", j);
                       else printf("Case #%d: Draw\n", j);
                  }
                  else {
                       if(X == 0) printf("Case #%d: O won\n", j);
                       if(O == 0) printf("Case #%d: X won\n", j);
                  }
                  X=0; O=0; j++;
       }
       return 0;
}
