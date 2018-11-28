#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {

  if (argc < 2) {
    ////cerr << "You should provide an input file" << endl;
    return 1;
  }

  ifstream myfile(argv[1]);
  if (!myfile.is_open()) {
    ////cerr << "Cannot open file" << endl;
    return 1;
  }

  int nb_tests;
  myfile >> nb_tests;

  for (int test_i = 1; test_i <= nb_tests; test_i++) {
    // Read input data
    int N, M;
    myfile >> N;
    myfile >> M;
    int lawn[N][M];
    for (int n = 0; n < N; n++) {
      for (int m = 0; m < M; m++) {
        int aij;
        myfile >> aij;
        lawn[n][m] = aij;
        //cerr << lawn[n][m];
      }
      //cerr << endl;
    }

    bool is_possible = true;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        int aij = lawn[i][j];
        //cerr << "aij: [" << i << "][" << j << "]: " << aij << endl;
        bool is_possible_aij = false;
        bool check_h = true, check_v = true;
        for (int k = 0; k < N; k++) {
          if (lawn[k][j] > aij) {
            check_h = false;
            break;
          }
        }
        for (int l = 0; l < M; l++) {
          if (lawn[i][l] > aij) {
            check_v = false;
            break;
          }
        }
        is_possible_aij = check_h || check_v;
        /*bool check_h_1 = true, check_h_2 = true, check_v_1 = true, check_v_2 = true;
        // Check horizontal beyond
        for (int k = i; k < N ; k++) {
          //cerr << k << " " << j << " " << lawn[k][j] << endl;
          if (lawn[k][j] > aij) {
            //cerr << "Check horizontal beyond Not possible" << endl;
            check_h_1 = false;
            break;
          }
        }
        // Check horizontal below
          for (int k = i; k >= 0; k--) {
            //cerr << k << " " << j << " " << lawn[k][j] << endl;
            if (lawn[k][j] > aij) {
              //cerr << "Check horizontal below Not possible" << endl;
              check_h_2 = false;
              break;
            }
          }
        // Check vertical beyond
          for (int l = j; l < M; l++) {
            //cerr << i << " " << l << " " << lawn[i][l] << endl;
            if (lawn[i][l] > aij) {
              //cerr << "Check vertical beyond Not possible" << endl;
              check_v_1 = false;
              break;
            }
          }
        // Check vertical below
          for (int l = j; l >= 0; l--) {
            //cerr << i << " " << l << " " << lawn[i][l] << endl;
            if (lawn[i][l] > aij) {
              //cerr << "Check vertical below Not possible" << endl;
              check_v_2 = false;
              break;
            }
          }
        is_possible_aij = check_h_1 || check_h_2 || check_v_1 || check_v_2;
        */
        //cerr << is_possible_aij << endl;
        if (!is_possible_aij) {
          //cerr << "Not possible" << endl;
          is_possible = false;
        }
      }
    }
    cout << "Case #" << test_i << ": " << (is_possible ? "YES" : "NO") << endl;
  }

  return 0;
}
