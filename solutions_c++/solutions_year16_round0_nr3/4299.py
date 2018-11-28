#include <bits/stdc++.h>

using namespace std;

int primos [] = {2, 3, 5, 7};

long long gera_num (int base, char *s) {
  long long x, b;
  
  x = 1;
  b = base;
  for (int i = 13; i >= 0; i--) {
    if (s[i] == '1')
      x += b;
    b = b * base;
  }
  return x + b;
}

bool nao_primo (long long x, int &div) {
  for (int i = 0; i < 4; i++) {
    if (x % primos[i] == 0) {
      div = primos[i];
      return true;
    }
  }
  return false;
}


int main () {
  ios_base::sync_with_stdio(false);
  int t, n, j, i, k, b, cont, resp[11], div;
  char s[16];
  
  cin >> t >> n >> j;
  cout << "Case #1:" << endl;
  
  cont = 0;
  for (i = 14; i >= 1 && cont < j; i--) {
    for (k = 0; k < i; k++)
      s[k] = '0';
    for (; k < 14; k++)
      s[k] = '1';
    s[14] = 0;
    
    do {
      bool achou_primo = false;
      for (b = 2; b <= 10 && !achou_primo; b++) {
        long long x = gera_num (b, s);
        if (nao_primo (x, div)) {
          resp[b] = div;
        }
        else
          achou_primo = true;
      }
      if (!achou_primo) {
        cout << "1" << s << "1";
        for (b = 2; b <= 10; b++)
          cout << " " << resp[b];
        cout << endl;
        cont++;
      }
    } while (next_permutation (s, s+14) && cont < j);
  }
  return 0;
}










