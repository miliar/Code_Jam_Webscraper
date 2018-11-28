#include <iostream>

using namespace std;

class Solver
{
public:
  Solver(){}
  void getInput(){
    cin >> X;
    cin >> R;
    cin >> C;
  }
  bool isPossible(){
    if(X == 1) return true;
    if((R*C)%X != 0) return false;
    if(X == 2) return true;
    if(X == 3){
      if(R == 1 || C == 1) return false;
      else return true;
    }
    if(X == 4){
      if(R < 3 || C < 3) return false;
      else return true;
    }
    if(X == 5){
      if(R < 4 || C < 4) return false;
      else return true;
    }
    if(X == 6){
      if(R < 5 || C < 5) return false;
      else return true;
    }
    return false;
  }
  void solve(){
    if(isPossible())
      cout << "GABRIEL";
    else
      cout << "RICHARD";
  }
  int X,R,C;
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