#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
using namespace std;

#define INF 0x7FFFFFFF
#define INFLL 0x7FFFFFFFFFFFFFFF
#define BIG 0x4F4F4F4F
#define PI acos(-1)
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())

typedef long long ll;
typedef unsigned long long ull;
typedef map<string, int> msi;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef pair<string, int> psi;

#define DEBUG(x) cout << #x << " : " << x << endl

#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair(x,y)
#define eps 1e-9

int main(int argc, char* argv[]) {
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int z = 1; z <= t; z++) {
    cout << "Case #" << z << ": ";
    char chess[4][4];
    int result = 0;
    bool done = true;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++) {
        cin >> chess[i][j];
        if (chess[i][j] == '.')
          done = false;
      }
    int flag = false;
    for (int i = 0; i < 4; i++) {
      int xx = 0, oo = 0;
      for (int j = 0; j < 4; j++) {
        if (chess[i][j] == 'X')
          xx++;
        if (chess[i][j] == 'O')
          oo++;
        if (chess[i][j] == 'T') {
          xx++;
          oo++;
        }
      }
      if (xx == 4) {
        cout << "X won" << endl;
        flag = true;
        break;
      }
      if (oo == 4) {
        cout << "O won" << endl;
        flag = true;
        break;
      }
    }
    if (flag)
      continue;
    for (int j = 0; j < 4; j++) {
      int xx = 0, oo = 0;
      for (int i = 0; i < 4; i++) {
        if (chess[i][j] == 'X')
          xx++;
        if (chess[i][j] == 'O')
          oo++;
        if (chess[i][j] == 'T') {
          xx++;
          oo++;
        }
      }
      if (xx == 4) {
        cout << "X won" << endl;
        flag = true;
        break;
      }
      if (oo == 4) {
        cout << "O won" << endl;
        flag = true;
        break;
      }
    }
    if (flag)
      continue;
    int xx = 0, oo = 0;
    for (int i = 0; i < 4; i++) {
      if (chess[i][i] == 'X')
        xx++;
      if (chess[i][i] == 'O')
        oo++;
      if (chess[i][i] == 'T') {
        xx++;
        oo++;
      }
    }
    if (xx == 4) {
      cout << "X won" << endl;
      flag = true;
    }
    if (oo == 4) {
      cout << "O won" << endl;
      flag = true;
    }
    if (flag)
      continue;
    xx = 0;
    oo = 0;
    for (int i = 0; i < 4; i++) {
      if (chess[i][3-i] == 'X')
        xx++;
      if (chess[i][3-i] == 'O')
        oo++;
      if (chess[i][3-i] == 'T') {
        xx++;
        oo++;
      }
    }
    if (xx == 4) {
      cout << "X won" << endl;
      flag = true;
    }
    if (oo == 4) {
      cout << "O won" << endl;
      flag = true;
    }
    if (flag)
      continue;
    if (!done) {
      cout << "Game has not completed" << endl;
      continue;
    }
    cout << "Draw" << endl;
  }
  return 0;
}
