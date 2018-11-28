#include <iostream>


using namespace std;

class Solver
{
public:
  Solver(){}
  void getInput(){
    cin >> N;
    m = new int[N];
    for(int i = 0; i < N; i ++){
      cin >> m[i];
    }
  }
  void solve(){
    int *iSub = new int[N];
    int iSubMax = 0;
    for(int i = 1; i < N; i++){
      iSub[i] = m[i-1] - m[i];
      if(iSub[i] < 0) iSub[i] = 0;
      if(iSub[i] > iSubMax) iSubMax = iSub[i];
    }
    int iResult1 = 0;
    int iResult2 = 0;
    for(int i = 1; i < N; i++){
      iResult1 += iSub[i];
      if(m[i-1] <= iSubMax){
        iResult2 += m[i-1];
      }else{
        iResult2 += iSubMax;
      }
      
      //cout << iResult2 << ',';
    }
    cout << iResult1 << " " << iResult2;
  }
  int N;
  int *m;
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