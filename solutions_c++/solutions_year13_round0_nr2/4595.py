#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T, N, M, max;
  int tmp =0;
  int** pattern;
  int* colMax;
  int* rowMax;
  cin >> T;
  for (int i=0; i<T; i++) {
    // Read data and fill row max
    cin >> N >> M;
    pattern = new int*[N];
    colMax = new int[M];
    rowMax = new int[N];
    for (int j=0; j<N; j++) {
      int* row = new int[M];
      max = 0;
      for (int k=0; k<M; k++) {
	cin >> row[k];
	max = ( (max > row[k]) ? max : row[k]);
      }
      rowMax[j] = max;
      pattern[j] = row;
    }

    // Fill colMax
    for (int j=0; j<M; j++) {
      max = 0;
      for (int k=0; k<N; k++) {
	max = ( (max > pattern[k][j]) ? max : pattern[k][j]);
      }
      colMax[j] = max;
    }

    // Check pattern validity using rowMax and colMax
    bool success = true;
    for (int j=0; j<N; j++) {
      for (int k=0; k<M; k++) {
	if (pattern[j][k] < rowMax[j] && pattern[j][k] < colMax[k]) {
	  // Not valid pattern
	  success = false;
	  break;
	}
      }
      if (!success) {
	break;
      }
    }	
  
    if (success) {
      cout << "Case #" << i+1 << ": YES" << endl;
    } else {
      cout << "Case #" << i+1 << ": NO" << endl;
    }

    // Delete allocations...
    for (int j=0; j<N; j++) {
      delete[] pattern[j];
    }
    delete[] pattern;
    delete[] colMax;
    delete[] rowMax;
  }
}
