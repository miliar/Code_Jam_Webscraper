#include <cstdio>

/* DEFINE:
  -1 = -1
   1 =  1
   i =  2
   j =  3
   k =  4
  -i = -2
  -j = -3
  -k = -4
*/
#define I 2
#define J 3
#define K 4

int convert(char a) {
  switch(a) {
  case 'i':
    return I;
  case 'j':
    return J;
  case 'k':
    return K;
  }
  return 0;
}

int prod(int a, int b) {
  int sign = 1;
  if(a < 0) {
    sign = -1;
    a = -a;
  }
  if(b < 0) {
    sign = -sign;
    b = -b;
  }

  if(a == 1) return sign*b;
  if(a == I) {
    if(b == 1) return sign*a;
    if(b == I) return -sign;
    if(b == J) return sign*K;
    if(b == K) return -sign*J;
  }
  if(a == J) {
    if(b == 1) return sign*a;
    if(b == I) return -sign*K;
    if(b == J) return -sign;
    if(b == K) return sign*I;
  }
  if(a == K) {
    if(b == 1) return sign*a;
    if(b == I) return sign*J;
    if(b == J) return -sign*I;
    if(b == K) return -sign;
  }
  return 0;
}

int pot(int base, int exp) {
  if(exp == 0 || base == 1) return 1;
  if(base == -1) {
    if(exp%2 == 0) return 1;
    return -1;
  }
  //Base eh I, J, K, -I, -J, -K
  int sign = 1;
  if(base < 0) {
    sign = -1;
    base = -base;
  }

  if(exp%2 == 0) {
    return pot(sign, exp)*pot(-1, exp/2);
  }
  return pot(sign, exp)*pot(-1, (exp-1)/2)*base;

}

char palavra[100000];

int multiplica(char word[], int com, int fim) {
  int m = 1;
  for(int i = com; i <= fim; i++)
    m = prod(m, convert(word[i]));
  return m;
}

int main() {
  int T;
  int X, L;
  int caso;
  int mult;
  bool res;
  char a;
  int tem[6];


  scanf("%d", &T);

  for(caso = 1; caso <= T; caso++) {

    scanf("%d %d\n", &L, &X);

    tem[I] = tem[J] = tem[K] = 0;

    for(int i = 0; i < L; i++) {
      scanf("%c", &a);
      palavra[i] = a;
      tem[convert(a)] = 1;
    }


    res = true;

    if(tem[I]+tem[J]+tem[K] < 2) {
      res = false;
    } else {
      int i = 1;
      int j = 0;
      mult = 1;
      int qual = I;

      while(i <= X) {
        while(j < L) {
          mult = prod(mult, convert(palavra[j]));
          if(mult == qual) {
            qual++;
            mult = 1;
          }
          j++;
          if(qual == K) break;
        }
        if(j == L) {
          j = 0;
          i++;
        }
        if(qual == K) break;
      }

      if(i == X+1) res = false;
      else {
        /*printf("j: %d  i: %d  X: %d\n", j, i, X);
        printf("mult: %d   mult2: %d  pot: %d   prod: %d\n",
               multiplica(palavra, j, L-1), multiplica(palavra, 0, L-1),
               pot(multiplica(palavra, 0, L-1), X-i), prod(multiplica(palavra, j, L-1), pot(multiplica(palavra, 0, L-1), X-i)));*/
        if(prod(multiplica(palavra, j, L-1), pot(multiplica(palavra, 0, L-1), X-i)) == K) res = true;
        else res = false;
      }
    }

    if(res)
      printf("Case #%d: YES\n", caso);
    else printf("Case #%d: NO\n", caso);
  }

  return 0;
}
