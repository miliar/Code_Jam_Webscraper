#include <cstdio>

using namespace std;

const int MAX_LX = 10005;

enum Quaternion {
  ONE = 0, I = 1, J = 2, K = 3,
  MONE = 4, MI = 5, MJ = 6, MK = 7
};

Quaternion p[MAX_LX];
Quaternion s[MAX_LX];

int T, L, X;

Quaternion read(char c) {
  switch (c) {
    case 'i': return I;
    case 'j': return J;
    case 'k': return K;
  }
  return ONE;
}

char write(Quaternion a) {
  char const table[8] = {
    '1', 'i', 'j', 'k',
    'O', 'I', 'J', 'K'
  };

  return table[a];
}

Quaternion neg(Quaternion a) {
  Quaternion const table[8] = {
    MONE, MI, MJ, MK,
    ONE, I, J, K
  };

  return table[a];
}

Quaternion mul(Quaternion a, Quaternion b) {
  Quaternion const table[4][4] = {
    {ONE, I, J, K},
    {I, MONE, K, MJ},
    {J, MK, MONE, I},
    {K, J, MI, MONE},
  };

  if (K < a) {
    return neg(mul(neg(a), b));
  }
  if (K < b) {
    return neg(mul(a, neg(b)));
  }

  return table[a][b];
}

Quaternion inv(Quaternion a) {
  Quaternion const table[8] = {
    ONE, MI, MJ, MK,
    MONE, I, J, K
  };

  return table[a];
}

Quaternion prod(int begin, int end) {
  /*
  printf("Calculating prod(%i, %i)\n", begin, end);
  printf("prod(%i, %i) = inv(%c) * %c = %c * %c = %c\n",
         begin, end,
         write(p[begin]), write(p[end]), write(inv(p[begin])),
         write(p[end]), write(mul(inv(p[begin]), p[end])));
  */

  return mul(inv(p[begin]), p[end]);
}

int main() {
  scanf("%i", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%i %i", &L, &X);
    p[0] = ONE;
    for (int l = 0; l < L * X; ++l) {
      char c;
      if (l < L) {
        scanf(" %c", &c);
        s[l] = read(c);
        // printf("wrote s[%i] = %c\n", l, write(s[l]));
        p[l + 1] = mul(p[l], s[l]);
      }
      else {
        // printf("Multiplying with s[%i] = %c\n", l % L, write(s[l % L]));
        p[l + 1] = mul(p[l], s[l % L]);
      }
      // printf("%i-th character is: %c\n", l, c);
      // printf("p[%i] = %c\n", l + 1, write(p[l + 1]));
    }

    bool found = false;

    for (int i = 1; i < L * X - 1; ++i) {
      for (int j = i + 1; j < L * X; ++j) {
        // printf("(0, %i) = %c,\n(%i, %i) = %c,\n(%i, %i) = %c\n", i, write(prod(0, i)), i, j, write(prod(i, j)), j, L * X, write(prod(j, L * X)));
        if (prod(0, i) == I && prod(i, j) == J && prod(j, L * X) == K) {
          found = true;
          break;
        }
      }
      if (found) {
        break;
      }
    }
    printf("Case #%i: ", t);
    if (found) {
      printf("YES");
    }
    else {
      printf("NO");
    }
    printf("\n");
  }

  return 0;
}
