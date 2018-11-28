#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
const int i = 1<<13;
int a[i], s[3], d[3];
int f[3][13][i];
int q, q1;
bool check(int t) {
  int w, e, r;
  for (w = 0; w < 3; w++) {
    d[w] = 0;
  }
  for (w = 0; w < q1; w++) {
    d[f[t][q][w]]++;
  }
  //for (w = 0; w < 3; w++) {
  //  cout << d[w] << " ";
 // }
  //cout << "   *\n";
  for (w = 0; w < 3; w++) {
    if (d[w] != s[w]) {
      return 0;
    }
  }
  return 1;
}


int main() {
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #else
    //freopen("bicone.in", "r", stdin);
    //freopen("bicone.out", "w", stdout);
  #endif // Vlad_kv
  int w, e, r, t, test, numTest;
  f[0][0][0] = 0;
  f[1][0][0] = 1;
  f[2][0][0] = 2;
  
  int c, v;
  
  char h[] = "RPS";
  
  for (w = 1; w < 13; w++) {
    for (e = 0; e < 3; e++) {
      r = (e - 1 + 3) % 3;
      v = 0;
      for (c = 0; c < 1<<(w - 1); c++) {
        if (h[f[e][w - 1][c]] < h[f[r][w - 1][c]]) {
          v = -1;
          break;
        }
        if (h[f[e][w - 1][c]] > h[f[r][w - 1][c]]) {
          v = 1;
          break;
        }
      }
      t = 0;
      if (v < 0) {
        for (c = 0; c < (1 << (w - 1)); c++) {
          f[e][w][t] = f[e][w - 1][c];
          t++;
        }
        for (c = 0; c < (1 << (w - 1)); c++) {
          f[e][w][t] = f[r][w - 1][c];
          t++;
        }
      } else {
        
        for (c = 0; c < (1 << (w - 1)); c++) {
          f[e][w][t] = f[r][w - 1][c];
          t++;
        }
        for (c = 0; c < (1 << (w - 1)); c++) {
          f[e][w][t] = f[e][w - 1][c];
          t++;
        }
        
        
      }
      
      
    }
  }
  
  
  
  cin >> numTest;
  for (test = 0; test < numTest; test++) {
    printf("Case #%d: ", test + 1);
    cin >> q;
    q1 = 1 << q;
    for (w = 0; w < 3; w++) {
      scanf("%d", &s[w]);
    }
    for (w = 0; w < 3; w++) {
      if (check(w)) {
        for (e = 0; e < q1; e++) {
          if (f[w][q][e] == 0) {
            cout << "R";
          }
          if (f[w][q][e] == 1) {
            cout << "P";
          }
          if (f[w][q][e] == 2) {
            cout << "S";
          }
          
        }
        cout << "\n";
        goto cnt;
      }
    }
    
    cout << "IMPOSSIBLE\n";
    cnt:;
  }
  return 0;
}