#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

vector<int> a;

const int LEFT = 1, RIGHT = 2, UP = 4, DOWN = 8;

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    int R, C;
    cin >> R >> C;
    char m[R][C];
    FOR (i, R) {
      string str;
      cin >> str;
      FOR (j, C)
        m[i][j] = str[j];
    }
    
    int forb[R][C];
    SET(forb, 0);
    FOR (i, R) {
      int j = 0;
      while (j < C && m[i][j] == '.')
        j++;
      if (j < C)
        forb[i][j] |= LEFT;
    }
    
    FOR (i, R) {
      int j = C - 1;
      while (j > -1 && m[i][j] == '.')
        j--;
      if (j > -1)
        forb[i][j] |= RIGHT;
    }

    FOR (j, C) {
      int i = 0;
      while (i < R && m[i][j] == '.')
        i++;
      if (i < R)
        forb[i][j] |= UP;
    }

    FOR (j, C) {
      int i = R - 1;
      while (i > -1 && m[i][j] == '.')
        i--;
      if (i > -1)
        forb[i][j] |= DOWN;
    }
    
    bool good = true;
    FOR (i, R)
      FOR (j, C)
        if (forb[i][j] == 15)
          good = false;

    int ret = 0;
    if (good) {
      FOR (i, R)
        FOR (j, C) {
          if (m[i][j] == '>' && (forb[i][j] & RIGHT) != 0) {
            ret++;
            continue;
          }

          if (m[i][j] == '<' && (forb[i][j] & LEFT) != 0) {
            ret++;
            continue;
          }

          if (m[i][j] == '^' && (forb[i][j] & UP) != 0) {
            ret++;
            continue;
          }

          if (m[i][j] == 'v' && (forb[i][j] & DOWN) != 0) {
            ret++;
            continue;
          }
        }
    }
    cout << "Case #" << (test + 1) << ": ";
    if (!good)
      cout << "IMPOSSIBLE";
    else
      cout << ret;
    cout << "\n";
  }
  return 0;
}
