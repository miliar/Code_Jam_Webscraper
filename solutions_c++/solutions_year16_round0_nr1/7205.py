#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

ifstream in("in.txt");

int main() {
  int t, n, j, copy, aux;
  bool found = false;
  bool seen[10];


  in >> t;

  for (int i = 0; i < t; i++) {
    in >> n;

    memset(seen, 0, 10);
    found = false;

    if (n == 0) {
      cout << "Case #" << i + 1 << ": INSOMNIA\n";
      continue;
    }

    aux = n;

    while (!found) {
      copy = aux;

      while (copy != 0) {
        seen[copy % 10] = true;

        copy = copy / 10;
      }

      for (j = 0; j < 10; j++) {
        if (seen[j] == false) {
          break;
        }
      }

      if (j == 10) {
        found = true;
      }
      else {
        aux += n;
      }
    }

    cout << "Case #" << i + 1 << ": " << aux << "\n";
  }

  return 0;
}
