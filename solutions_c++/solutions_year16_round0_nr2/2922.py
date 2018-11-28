#include <bits/stdc++.h>
using namespace std;

int main() {
  int T; scanf("%d",&T);
  for (int tt=1; tt<=T; tt++) {
    char S[105]; scanf("%s",S);
    int Len = strlen(S);
    int numMoves = 0;
    while (true) {
      bool hasMinus = false;
      for (int i=0; i<Len; i++) {
        if (S[i] == '-') {
          hasMinus = true;
          break;
        }
      }
      if (!hasMinus) break;
      if (S[0] == '+') {
        for (int i=0; i<Len && S[i]=='+'; i++)
          S[i] = '-';
      }else {
        int minusPos = Len;
        for (int i=Len-1; i>=0; i--) {
          if (S[i] == '-') {
            minusPos = i;
            break;
          }
        }
        char T[105]; int tptr=0;
        for (int i=minusPos; i>=0; i--) {
          T[tptr++] = S[i]=='+' ? '-' : '+';
        }
        T[tptr] = '\0';
        for (int i=0; i<tptr; i++)
          S[i] = T[i];
      }
      numMoves++;
    }
    printf("Case #%d: %d\n",tt,numMoves);
  }
  return 0;
}
