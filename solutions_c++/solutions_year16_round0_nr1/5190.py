#include <bits/stdc++.h>

using namespace std;

int resolve (int n) {
  int x, cont, i, d;
  bool showup[10];
  
  for (i = 0; i < 10; i++)
    showup[i] = false;
  i = cont = 0;
  
  while (cont != 10) {
    i++;
    x = n * i;
    while (x > 0) {
      d = x % 10;
      x = x / 10;
      if (!showup[d])
        cont++;
      showup[d] = true;
    }
  }
  return (n * i);
}

int main () {
  ios_base::sync_with_stdio(false);
  int t, i, n, caso;
  
  cin >> t;
  
  for (caso = 1; caso <= t; caso++) {
    cin >> n;
    if (n == 0)
      cout << "Case #" << caso << ": INSOMNIA" << endl;
    else
      cout << "Case #" << caso << ": " << resolve (n) << endl;
  }
  
  return 0;
}










