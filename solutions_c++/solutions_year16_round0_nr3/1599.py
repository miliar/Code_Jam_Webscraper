#include <bits/stdc++.h>
using namespace std;

int main() {
  int cont = 0;
  bitset<33> b;
  b.set(0);
  b.set(31);
  printf("Case #1:\n");
  while(!b[33] && cont <500) {
    int ok = 1, k = 0;
    long long d[11];

    for (int i=2; i<=10 && ok; i++) {
      int p = 0;
      for (long long j = 3; j <= 100000; j+=2) {

      long long aux = 1;
      long long n = 0;

      for (int k = 0; k<32; k++) {
        if(b[k]) n = (n+aux)%j;
        aux = (aux*i)%j;
      }
        if(!(n)) {
          p=1;
          d[i]=j;
          break;
        }
      }
      if(!p) ok = 0;
    }

    if (ok) {
      cont++;
      for (int j = 31; j>=0; j--) {
        printf("%d", b.test(j));
      }
      for (int j = 2; j<=10; j++) printf(" %lld", d[j]);
      printf("\n");
    }

    int i = 1;
    while(1) {
      b.flip(i);
      if(b[i]) break;
      i++;
    }
  }
}
