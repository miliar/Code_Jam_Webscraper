#include<stdlib.h>
#include<iostream>
#include<algorithm>

const int N = 100;


using namespace std;
int main() {
  
  int mRows[N];
  int mCols[N];
  int M[N][N];
  int nCases = 0;
  cin >> nCases;
  
  for (int numCase = 0; numCase < nCases; ++numCase){
    
    int X, Y;
    cin >> X >> Y;
    
    // Reset max
    for (int i = 0; i < X; ++i) mRows[i] = 0;
        for (int j = 0; j < Y; ++j) mCols[j] = 0;
  
    // Compute the max
    for (int i = 0; i < X; ++i){
      for (int j = 0; j < Y; ++j){
        int value;
        cin >> value;
        M[i][j] = value;
        mRows[i] = max(mRows[i], value);
        mCols[j] = max(mCols[j], value);
      }
    }

    // Compute the max
    bool sol = true;
    for (int i = 0; i < X; ++i){
      for (int j = 0; j < Y; ++j){
          if (M[i][j] < mRows[i] && M[i][j] < mCols[j]){
            sol = false;
            break;
          }

      }
    }
    if (sol)
        cout << "Case #" <<numCase+1 << ": YES" << endl;
    else
        cout << "Case #" <<numCase+1 << ": NO" << endl;


  }


  return EXIT_SUCCESS;
}
