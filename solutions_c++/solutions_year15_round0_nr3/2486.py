//#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream cin("C-small-attempt3.in");
ofstream cout("C-small.out");

int main() {
    int T;
    cin >> T;
    int A[10001];
    int B[10001];
    int B2[10001];
    int C[10001];
    int table[8][8] = {
      {0,1,2,3,4,5,6,7},
      {1,4,3,6,5,0,7,2},
      {2,7,4,1,6,3,0,5},
      {3,2,5,4,7,6,1,0},
      {4,5,6,7,0,1,2,3},
      {5,0,7,2,1,4,3,6},
      {6,3,0,5,2,7,4,1},
      {7,6,1,0,3,2,5,4}
    };
    for (int t=0; t<T; t++) {
      int L,X; cin >> L >> X;
      string s; cin >> s; string sp = s;
      for (int k=1; k<X; k++)
        sp = sp + s;
      int ttcnt = sp.size();
      for (int i=0; i<ttcnt; i++) {
        if (sp[i] == 'i') A[i] = 1;
        else if (sp[i] == 'j') A[i] = 2;
        else A[i] = 3;
      }
      int lval = 0; int rval = 0;
      for (int i=0; i<ttcnt; i++) {
        int ri = ttcnt-i-1;
        B[i] = table[lval][A[i]]; C[ri] = table[A[ri]][rval];
        lval = B[i]; rval = C[ri];
      }
      bool found = false;
      for (int i=0; i<ttcnt-2; i++) { int mid=0;
        for (int k=i+1; k<ttcnt-1; k++) { B2[k] = table[mid][A[k]]; mid = B2[k]; }
        for (int j=i+2; j<ttcnt; j++) {
          int left = B[i]; mid = B2[j-1]; int right = C[j];
          if (left == 1 && mid == 2 && right == 3) { found = true; break; }
        }
      }
      cout << "Case #" << t+1 << ": ";
      if (found) cout << "YES"; else cout << "NO"; cout << endl;
    }
return 0;
}
