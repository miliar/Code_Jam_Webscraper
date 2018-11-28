#include <iostream>
using namespace std;

class Solver
{
public:
  Solver(){}
  void getInput(){
    cin >> R;
    cin >> C;
    cin >> W;
  }
  void solve(){
    if(W == 1){
      cout << R * C;
      return;
    }
    if(R == 1){
      int iCost = C/W;
      if(C%W > 0) iCost += 1;
      iCost+= (W-1);
      cout << iCost;
    }
    /*int iCost = R/W + C/W + (R%W) * (C/W) + (R/W) * (C%W) + (R%W) * (C%W);
    cout << iCost + W;*/
  }
  int R,C,W;

};

int main()
{
  int N;
  cin >> N;
  for (int i = 0; i < N; i++){
    Solver mySolver;
    mySolver.getInput();
    cout << "Case #" << i+1 << ": ";
    mySolver.solve();
    cout << endl;
  }
  return 0;
}