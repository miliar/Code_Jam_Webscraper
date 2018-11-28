#include <iostream>
#include <vector>

using namespace std;

enum Quaternion {
  ONE = 0,
  I = 1,
  J = 2,
  K = 3,
  MINUS_ONE = 4,
  MINUS_I = 5,
  MINUS_J = 6,
  MINUS_K = 7
};

int mult[8][8] =
{{ONE,       I,         J,         K,         MINUS_ONE, MINUS_I,   MINUS_J,   MINUS_K  },
 {I,         MINUS_ONE, K,         MINUS_J,   MINUS_I,   ONE,       MINUS_K,   J        },
 {J,         MINUS_K,   MINUS_ONE, I,         MINUS_J,   K,         ONE,       MINUS_I  },
 {K,         J,         MINUS_I,   MINUS_ONE, MINUS_K,   MINUS_J,   I,         ONE      },
 {MINUS_ONE, MINUS_I,   MINUS_J,   MINUS_K,   ONE,       I,         J,         K        },
 {MINUS_I,   ONE,       MINUS_K,   J,         I,         MINUS_ONE, K,         MINUS_J  },
 {MINUS_J,   K,         ONE,       MINUS_I,   J,         MINUS_K,   MINUS_ONE, I        },
 {MINUS_K,   MINUS_J,   I,         ONE,       K,         J,         MINUS_I,   MINUS_ONE}};

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int l, x;
    cin >> l >> x;
    vector<int> a(l);
    for (int i = 0; i < l; ++i) {
      char c;
      cin >> c;
      a[i] = (c == 'i') ? 1 : ((c == 'j') ? 2 : 3);
    }

    int shortProd = a[0];
    for (int i = 1; i < l; ++i) {
      shortProd = mult[shortProd][a[i]];
    }
    int longProd = shortProd;
    for (int i = 1; i < x; ++i) {
      longProd = mult[longProd][shortProd];
    }
    if (longProd != MINUS_ONE) {
      cout << "Case #" << tt << ": NO" << endl;
      continue;
    }

    vector<int> minFromStart(8, -1);
    {
      vector<bool> seen(8, false);
      int prod = ONE;
      int cur = 0;
      while (!seen[prod]) {
        seen[prod] = true;
        for (int i = 0; i < l; ++i) {
          ++cur;
          prod = mult[prod][a[i]];
          if (minFromStart[prod] == -1) {
            minFromStart[prod] = cur;
          }
        }
      }
    }

    vector<int> minFromEnd(8, -1);
    {
      vector<bool> seen(8, false);
      int prod = ONE;
      int cur = 0;
      while (!seen[prod]) {
        seen[prod] = true;
        for (int i = l - 1; i >= 0; --i) {
          ++cur;
          prod = mult[a[i]][prod];
          if (minFromEnd[prod] == -1) {
            minFromEnd[prod] = cur;
          }
        }
      }
    }

    bool possible =
         (minFromStart[I] != -1)
      && (minFromEnd[K] != -1)
      && (x > 20 || minFromStart[I] + minFromEnd[K] < l*x);
    cout << "Case #" << tt << ": " << (possible ? "YES" : "NO") << endl;
  }
  return 0;
}
