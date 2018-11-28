#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>

#define NDEBUG

int max(int a , int b) {
  return (a > b) ? a : b;
}

int min(int a , int b) {
  return (a < b) ? a : b;
}

using namespace std;

const char INPUT[] = "HelloWorld.inp";
const char OUTPUT[] = "HelloWorld.out";

int main() {
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);

  int numTest;
  cin >> numTest;

  for (int idTest = 0; idTest < numTest; ++ idTest) {
    int k, c, s;
    cin >> k >> c >> s;

    cout << "Case #" << idTest + 1 << ": ";
    if (k <= s) {
      long long tmp = 1;
      for (int id = 1; id < c; ++ id) {
        tmp *= k;
      }
      for (int id = 0; id < k; ++ id) {
        cout << tmp * id + 1 << " ";
      }
      cout << endl;
    } else if (k != 2 || c == 1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << "2" << endl;
    }
  }

  return 0;
}
