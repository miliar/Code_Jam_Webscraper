#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]){
  string token;
  ifstream f(argv[1]);
  int cases;
  double C, F, X;
  double CPS = 2;
  double TNF = 0;
  double TWF = 0;
  double T = 0;
  double TF = 0;

  //    cout << setprecision(7);

  f >> token;
  cases = atoi(token.c_str());

  for (int i = 1; i <= cases; i++){
    f >> token;
    C = atof(token.c_str());
    f >> token;
    F = atof(token.c_str());
    f >> token;
    X = atof(token.c_str());

    T = 0;
    TNF = X / CPS;
    TF = C / CPS;
    CPS += F;
    TWF = (X / CPS) + (TF);
    while(TNF > TWF){
      T+= TF;
      TNF = X / CPS;
      TF = C / CPS;
      CPS += F;
      TWF = (X / CPS) + (TF);
    }
    T+= TNF;
    cout << "Case #" << i << ": ";
    cout << setprecision(10);
    cout << T << endl;
    CPS = 2;
  }
}
