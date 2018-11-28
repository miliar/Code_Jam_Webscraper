#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <fstream>
#include <ctime>
using namespace std;
const int n = 1000;
int a[n];
bool a1[n], f[40];
int d[11];
int h[1000][40];
int h1[1000][11];
int main() {
  srand(time(0));
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
  int q, w, e, r, t = 0, needToSch, alSch = 0, c, v;
  for (w = 0; w < n; w++) {
    a1[w] = 1;
  }
  for (w = 2; w < n; w++) {
    if (a1[w]) {
      a[t] = w;
      t++;
      for (e = w * 2; e < n; e += w) {
        a1[e] = 0;
      }
    }
  }
  /*
  cout << t << "\n---\n";
  for (w = 0; w < t; w++) {
    cout << a[w] << " ";
  }
  cout << "\n";
  */
  
  ifstream z("input.txt");
  z >> q;
  z >> q >> needToSch;
  z.close();
  ofstream x("output.txt");
  int allTr = 0;
  long long realVal;
  while (alSch < needToSch) {
    //cout << "\n";
    allTr++;
    f[0] = 1;
    for (w = 1; w < q; w++) {
      f[w] = rand()%2;
    }
    f[q - 1] = 1;
    for (w = 2; w < 11; w++) {
      realVal = 0;
      for (e = 0; e < q; e++) {
        realVal = min(((long long)1)<<50, realVal * w + f[e]);
      }
      //cout << realVal << " ";
      for (e = 0; e < t; e++) {
        c = 0;
        for (r = 0; r < q; r++) {
          c = (c * w + f[r]) % a[e];
        }
        if (c == 0) {
          //cout << realVal << " " << a[e] << "\n";
          /*if (realVal % a[e] != 0) {
            cout << realVal << "  ###########\n\n\n\n";
          }*/
          break;
        }
      }
      if (e == t) {
        goto cnt;
      }
      if (realVal <= a[e]) {
        goto cnt;
      }
      //cout << a[e] << " !!!\n";
      d[w] = a[e];
      //cout << w << " " << d[w] << "  %%%%%\n";
    }
    
    bool b;
    for (c = 0; c < alSch; c++) {
      b = 0;
      for (v = 0; v < q; v++) {
        if (f[v] != h[c][v]) {
          b = 1;
          break;
        }
      }
      if (!b) {
        goto cnt;
      }
    }
    for (e = 0; e < q; e++) {
      h[alSch][e] = f[e];
    }
    for (e = 2; e < 11; e++) {
      h1[alSch][e] = d[e];
      //cout << d[e] << " ???\n";
    }
    alSch++;
    //cout << alSch << "   " << realVal << "\n";
    
    cnt:;
  }
  
  //cout << "\n" << allTr << "\n";
  
  cout << "Case #1:\n";
  
  for (w = 0; w < needToSch; w++) {
    for (e = 0; e < q; e++) {
      cout << h[w][e];
    }
    cout << " ";
    for (e = 2; e < 11; e++) {
      cout << h1[w][e] << " ";
    }
    cout<< "\n";
    
    for (e = 2; e < 11; e++) {
      realVal = 0;
      for (r = 0; r < q; r++) {
        realVal = realVal * e + h[w][r];
      }
      //if (realVal % h1[w][e] != 0) {
      //  cout << realVal << "  " << h1[w][e] << "@@@@@@@@@@\n";
      //}
      
    }
    
    
    
    
  }
  
  //x.close();
  
  
  return 0;
}