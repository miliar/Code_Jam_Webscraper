#include <iostream>
#include <string>
#include <cmath>
using namespace std;

unsigned int g_Table[15];
class Solver
{
public:
  Solver(){}
  void getInput(){
    cin >> sInput;
  }
  void solve(){
    unsigned int iSize = sInput.size();
    if(iSize == 1){
      cout << sInput;
      return;
    }
    bool bZeroEnd = false;
    if(sInput[iSize-1] == '0'){
      bZeroEnd = true;
      unsigned long long iTemp = stoull(sInput);
      sInput = to_string((unsigned long long)(iTemp-1));
      iSize = sInput.size();
      if(iSize == 1){
        cout << iTemp;
        return;
      }
    }
    bool bReverse = false;
    unsigned int iFrontSum = 0;
    unsigned int iBackSum = 0;
    for(int i = 0; i < iSize; i++){
      if(i == 0){
        if(sInput[i]>'1')
          bReverse = true;
        iFrontSum += (sInput[i] - '1')* pow((double)10,i);
      }else if(i<iSize/2){
        if(sInput[i]>'0')
          bReverse = true;
        iFrontSum += (sInput[i] - '0')* pow((double)10,i);
      }else{
        iBackSum += (sInput[i] - '0');
        iBackSum *= 10;
      }
    }
    iBackSum /= 10;
    unsigned int iSum = g_Table[iSize-1] + iFrontSum + iBackSum;
    if(bReverse) iSum++;
    if(bZeroEnd) iSum++;
    cout << iSum;
  }
  string sInput;

};

int main()
{
  g_Table[0] = 1;
  for(int i = 1; i < 15; i++){
    if(i%2 == 1){
      g_Table[i] = pow((double)10, i/2) + pow((double)10, i/2+1) - 1;
    }else{
      g_Table[i] = pow((double)10, i/2) + pow((double)10, i/2) - 1;
    }
  }
  for(int i = 13; i >=1; i--){
    for(int j = i + 1; j < 15; j++){
      g_Table[j] += (g_Table[i]);
    }
  }
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