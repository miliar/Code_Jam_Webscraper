#include <cstdio>

using namespace std;

int main() {
  int T, S;
  char c;
  int p;
  int pessoas, adicionadas;
  int caso = 1;
  scanf("%d", &T);

  while(caso <= T) {
    scanf("%d ", &S);
    pessoas = adicionadas = 0;

    for(int i = 0; i <= S; i++) {
      scanf("%c", &c);
      p = c-'0';
      if(pessoas >= i || p == 0) {
          pessoas += p;
      } else {
        adicionadas += i-pessoas;
        pessoas += i-pessoas;
        pessoas += p;
      }
    }

    printf("Case #%d: %d\n", caso, adicionadas);
    caso++;
  }
  return 0;
}
