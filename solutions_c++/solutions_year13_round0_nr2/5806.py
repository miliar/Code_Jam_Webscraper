//
//  Google Jam 2013
//
//  Problem: Qualif. A
//   
//  Author: Marçal Sola

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define max(X,Y) ((X >= Y) ? X : Y)
#define min(X,Y) ((X < Y) ? X : Y)

int main (void) {
  
  int cases; 
  cin >> cases; 
  
  for (int ncase = 1; ncase <= cases; ncase++) {
    int rows, cols;
    cin >> rows >> cols; 

    vector<int> hor_lower(rows, 100);
    vector<int> ver_lower(cols, 100);
    vector<int> hor_higher(rows, 0);
    vector<int> ver_higher(cols, 0);

    bool possible = true; 
    for (int r = 0; r < rows; r++ ) {
      for (int c = 0; c < cols; c++) {
        int sq;
        cin >> sq;

        if (sq < hor_higher[r]) {
          ver_lower[c] = min(ver_lower[c], sq);
          if (sq < ver_higher[c]) possible = false;
        }
        if (sq < ver_higher[c]) {
          hor_lower[r] = min(hor_lower[r], sq);
          if (sq < hor_higher[r]) possible = false;
        }
        if (sq > hor_lower[r] or sq > ver_lower[c]) {
          possible = false;
        }
        hor_higher[r] = max(hor_higher[r], sq);
        ver_higher[c] = max(ver_higher[c], sq);
      }
    }
    
    // end
    if (possible) cout << "Case #" << ncase << ": YES" << endl;
    else  cout << "Case #" << ncase << ": NO" << endl;
  }

  return 0;
}
