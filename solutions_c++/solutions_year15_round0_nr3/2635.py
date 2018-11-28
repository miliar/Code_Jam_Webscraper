#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <math.h>

using namespace std;

bool sign[128][128] = {0};
char mat[128][128] = {0};

void Init() {
  mat['1']['1'] = '1'; mat['1']['i'] = 'i'; mat['1']['j'] = 'j'; mat['1']['k'] = 'k';
  mat['i']['1'] = 'i'; mat['i']['i'] = '1'; mat['i']['j'] = 'k'; mat['i']['k'] = 'j';
  mat['j']['1'] = 'j'; mat['j']['i'] = 'k'; mat['j']['j'] = '1'; mat['j']['k'] = 'i';
  mat['k']['1'] = 'k'; mat['k']['i'] = 'j'; mat['k']['j'] = 'i'; mat['k']['k'] = '1';

  sign['i']['i'] = true;
  sign['i']['k'] = true;
  sign['j']['j'] = true;
  sign['j']['i'] = true;
  sign['k']['k'] = true;
  sign['k']['j'] = true;
}

char multi(char a, char b) {
  bool minus = false;
  if (a < 0) {
    a = 0-a;
    minus = !minus;
  }
  if (b < 0) {
    b = 0-b;
    minus = !minus;
  }
  if (sign[a][b]) {
    minus = !minus;
  }
  if (minus) {
    return 0 - mat[a][b];
  }
  return mat[a][b];
}

int main() {
  Init();
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";
    int L, X;
    cin >> L >> X;
    string tmp;
    cin >> tmp;
    char now = '1';
    char need = 'i';
    bool reach = false;
    for (int j = 0; j < X; ++j) {
      for (int k = 0; k < L; ++k) {
        now = multi(now, tmp[k]);
        if (now == need) {
          if (need == 'i') {
            need = 'j';
          } else if (need == 'j') {
            need = '0';
            reach = true;
          }
          now = '1';
        }
      }
    }
    if (reach && now == 'k') {
      cout << "YES";
    } else {
      cout << "NO";
    }
    cout << endl;
  }
}
