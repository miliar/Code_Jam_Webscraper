#include <stdio.h>

using namespace std;

// 1 = 1
// 2 = i
// 3 = j
// 4 = k

int conv(char c) {
  if (c == '1')
    return 1;
  else if (c == 'i')
    return 2;
  else if (c == 'j')
    return 3;
  else if (c == 'k')
    return 4;
  else 
    return -1;
}

int mult(int x, int y) {
  int aux, a, b;
  if (x < 0 && y < 0)
    aux = 1;
  else if ((x < 0 && y > 0) || (x > 0 && y < 0))
    aux = -1;
  else
    aux = 1;
  if (x < 0) {
    a = -x;
  } else {
    a = x;
  }
  if (y < 0) {
    b = -y;
  } else {
    b = y;
  }
  if (a == 1 && b == 1) {
    return 1 * aux;
  } else if (a == 1 && b == 2) {
    return 2 * aux;
  } else if (a == 1 && b == 3) {
    return 3 * aux;
  } else if (a == 1 && b == 4) {
    return 4 * aux;
  } else if (a == 2 && b == 1) {
    return 2 * aux;
  } else if (a == 2 && b == 2) {
    return -1 * aux;
  } else if (a == 2 && b == 3) {
    return 4 * aux;
  } else if (a == 2 && b == 4) {
    return -3 * aux;
  } else if (a == 3 && b == 1) {
    return 3 * aux;
  } else if (a == 3 && b == 2) {
    return -4 * aux;
  } else if (a == 3 && b == 3) {
    return -1 * aux;
  } else if (a == 3 && b == 4) {
    return 2 * aux;
  } else if (a == 4 && b == 1) {
    return 4 * aux;
  } else if (a == 4 && b == 2) {
    return 3 * aux;
  } else if (a == 4 && b == 3) {
    return -2 * aux;
  } else if (a == 4 && b == 4) {
    return -1 * aux;
  } 
  return -1;
}

int main() {
  char temp[10003];
  int in[10003], x, i, j, t, c, l, flagI, flagJ, flagK, aux, obj, total, sum;

  scanf("%d", &t);
  c = 1;
  while (t--) {
    obj = 2;
    flagK = flagJ = flagI = 0;
    scanf("%d %d", &l, &x);
    scanf("%s", temp);
    total = 1;
    for (i = 0; i < l; i++) {
      in[i] = conv(temp[i]);
      total = mult(total, in[i]);
    }
    aux = 1;
    for (i = 0; i < x; i++) {
      for (j = 0; j < l; j++) {
	aux = mult(aux, in[j]);
	if (aux == obj) {
	  if (obj == 2) {
	    flagI = 1;
	    aux = 1;
	    obj++;
	  } else if (obj == 3) {
	    flagJ = 1;
	    aux = 1;
	    obj++;
	  }
	}
      }
      if (obj == 4) {
	break;
      }
    }
    if (obj == 4) {
      if (i + 1 < x) {
	sum = 1;
	for (j = i + 1; j < x; j++) {
	  sum = mult(sum, total);
	}
	aux = mult(aux, sum);
      }
    }
    if (aux == obj)
      flagK = 1;
    if (flagI * flagJ * flagK == 1)
      printf("Case #%d: YES\n", c);
    else
      printf("Case #%d: NO\n", c);
    c++;
  }


  return 0;
}
