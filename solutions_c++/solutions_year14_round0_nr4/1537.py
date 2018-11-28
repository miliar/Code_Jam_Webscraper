#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

const char* input  = "D-large.in";
//const char* input  = "opa.txt";
const char* output = "D-large.out";


int main(int argc, char** argv) {
  
  ifstream I(input);
  ofstream O(output);

  int T; I >> T;
  for (int t = 0; t < T; ++t) {

    vector<double> nr, nd; // Naomi's blocks (r: regular, d: deceitful)
    vector<double> kr, kd; // Kevin's blocks (r: regular, d: deceitful)
    
    int N; I >> N;
    nr.resize(N); nd.resize(N);
    kr.resize(N); kd.resize(N);

    for (int i = 0; i < N; ++i) I >> nr[i];
    for (int i = 0; i < N; ++i) I >> kr[i];

    sort(nr.begin(), nr.end());
    sort(kr.begin(), kr.end());
    
    for (int i = 0; i < N; ++i) nd[i] = nr[i];
    for (int i = 0; i < N; ++i) kd[i] = kr[i];

    int Sr = 0, Sd = 0;;  // Naomi's scores (r: regular, d: deceitful)

    // play regular
    for (int i = 0; i < N; ++i) {
      int j;
      for (j = 0; j < N; ++j) {
        if (kr[j] > nr[i]) {
          kr[j] = -1;
          break;
        }
      }
      if (j == N)
        ++Sr;
    }

    // play deceitful
    int nm = 0, nM = N - 1;
    int km = 0, kM = N - 1;
    for (int i = 0; i < N; ++i) {
      /*
      cout << "******************************" << endl;
      for (int k = 0; k < N; ++k)
          cout << nd[k] << " ";
      cout << endl;
      for (int k = 0; k < N; ++k)
          cout << kd[k] << " ";
      cout << endl;
      */
      if (nd[nm] < kd[km]) {
        nd[nm] = kd[kM] = -1;
        ++nm;
        --kM;
      }
      else {
        ++Sd;
        nd[nm] = kd[km] = -1;
        ++nm;
        ++km;
      }
    }


    O << "Case #" << (t + 1) << ": " << Sd << " " << Sr << endl;
    cout << "Case #" << (t + 1) << ": " << Sd << " " << Sr << endl;
  }


  I.close();
  O.close();
  return 0;
}
