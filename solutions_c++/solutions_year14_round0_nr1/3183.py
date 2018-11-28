#include <iostream>

using namespace std;

const unsigned int SIZE     = 4;
const unsigned int ATTEMPTS = 2;

int main() {
  // Read in # test cases
  unsigned int T;
  cin >> T;
  for (unsigned int i = 1; i <= T; ++i) {
    // Parse inputs
    int answers[ATTEMPTS];
    int grids[ATTEMPTS][SIZE][SIZE];
    for (unsigned int attempt = 0; attempt < ATTEMPTS; ++attempt) {
      cin >> answers[attempt];
      for (unsigned int grid_row = 0; grid_row < SIZE; ++grid_row) {
        for (unsigned int grid_col = 0; grid_col < SIZE; ++grid_col) {
          cin >> grids[attempt][grid_row][grid_col];
        }
      }
    }   
  
    // Compute answers    
    bool numbers[SIZE * SIZE];
    for (unsigned int j = 0; j < SIZE * SIZE; ++j) {
      numbers[j] = false;
    } 

    // Record first answer
    for (unsigned int j = 0; j < SIZE; ++j) {
      numbers[grids[0][answers[0] - 1][j] - 1] = true;
    }

    // See how many hits for second answer
    unsigned int finalAns = 0;
    unsigned int numHits = 0;
    for (unsigned int j = 0; j < SIZE; ++j) {
      if (numbers[grids[1][answers[1] - 1][j] - 1]) {
	finalAns = grids[1][answers[1] - 1][j];
	++numHits;
      }
    }

    // Print answers
    cout << "Case #" << i << ": ";
    if (numHits == 0) {
      cout << "Volunteer cheated!";
    } else if (numHits == 1) {
      cout << finalAns;
    } else {
      cout << "Bad magician!";
    }
    cout << "\n";
  }

  return 0;
}
