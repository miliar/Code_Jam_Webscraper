#include <iostream>
#include <iomanip>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

void solveCase(int n){
  double C, F, X, answer = 0.0, S = 2.0;
  double completion, farm, farmAndC;

  cin >> C >> F >> X;
  while(true){
    completion = X / S; // Time for completion
    farm = C / S; // Time for next farm
    farmAndC = farm + X / (S + F); // Time for completion after new farm
    if(completion < farmAndC){
      answer += completion;
      break;
    }
    answer += farm;
    S += F;
  }

  cout << "Case #" << n << ": " << fixed << setprecision(7) << answer << endl;
}

int main(int argc, char** argv){
  int T;
  cin >> T;
  for(int i=0; i<T; i++){
    solveCase(i+1);
  }
  return 0;
}
