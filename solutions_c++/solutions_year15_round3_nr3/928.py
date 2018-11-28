#include <iostream>
#include <vector>
using namespace std;

class Solver
{
public:
  Solver(){}
  void getInput(){
    cin >> C >> D >> V;
    iCoin = new int[D];
    for(int i = 0; i < D; i++){
      cin >> iCoin[i];
    }
  }
  void solve(){
    if(C == 1){
      int iCount = 0;
      bool *bValue = new bool[V+1]();
      for(int i = 0; i < D; i++){
        for(int j = V; j > 0; j--){
          if(bValue[j] && j+iCoin[i] <= V)
            bValue[j+iCoin[i]] = true;
        }
        bValue[iCoin[i]] = true;
      }
      for(int i = 1; i <= V; i++){
        if(!bValue[i]){
          iCount++;
          for(int j = V; j > 0; j--){
            if(bValue[j] && j+i <= V)
              bValue[j+i] = true;
          }
          bValue[i] = true;
        }
      }
      cout << iCount;
    }
  }
  int C,D,V;
  int *iCoin;
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