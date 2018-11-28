#include <iostream>
#include <string>

using namespace std;

class Solver
{
public:
  enum Quaternions{
    QUATERNIONS_i = 2,
    QUATERNIONS_j,
    QUATERNIONS_k
  };
  Solver(){}
  void getInput(){
    cin >> L;
    cin >> X;
    for(int i = 0; i < L; i++){
      char cInput;
      cin >> cInput;
      switch(cInput){
        case'i': qInput[i] = QUATERNIONS_i; break;
        case'j': qInput[i] = QUATERNIONS_j; break;
        case'k': qInput[i] = QUATERNIONS_k; break;
      }
    }
  }
  int multiply(int x, int y){
    int iPosNega = 1;
    if(x < 0){
      x = -x;
      iPosNega *= -1;
    }
    if(y < 0){
      y = -y;
      iPosNega *= -1;
    }
    if(x==QUATERNIONS_i){
      if(y==QUATERNIONS_i) return -1 * iPosNega;
      else if(y==QUATERNIONS_j) return QUATERNIONS_k * iPosNega;
      else if(y==QUATERNIONS_k) return -QUATERNIONS_j * iPosNega;
      else return QUATERNIONS_i * iPosNega;
    }else if(x==QUATERNIONS_j){
      if(y==QUATERNIONS_i) return -QUATERNIONS_k * iPosNega;
      else if(y==QUATERNIONS_j) return -1 * iPosNega;
      else if(y==QUATERNIONS_k) return QUATERNIONS_i * iPosNega;
      else return QUATERNIONS_j * iPosNega;
    }else if(x==QUATERNIONS_k){
      if(y==QUATERNIONS_i) return QUATERNIONS_j * iPosNega;
      else if(y==QUATERNIONS_j) return -QUATERNIONS_i * iPosNega;
      else if(y==QUATERNIONS_k) return -1 * iPosNega;
      else return QUATERNIONS_k * iPosNega;
    }else return iPosNega * y;
  }  
  void solve(){
    int qStringValue = qInput[0];
    for(int i = 1; i < L; i++){
      qStringValue = multiply(qStringValue, qInput[i]);
    }
    int iReapetTimes;
    switch(qStringValue){
    case 1: iReapetTimes = 1;
    case -1: iReapetTimes = 2;
    default: iReapetTimes = 4;
    }
    int iRealSize;
    if(X/(iReapetTimes*3) < 2)
      iRealSize = X;
    else
      iRealSize = iReapetTimes*3 + X%(iReapetTimes*3);
    //iRealSize = X;
    int *qReal = new int[iRealSize * L];
    for(int i = 0; i < iRealSize; i++)
      for(int j = 0; j < L; j++)
        qReal[i*L+j] = qInput[j];
    iRealSize *= L;

    int iIndex = 0;
    int qFront = qReal[iIndex];
    while(qFront != QUATERNIONS_i){
      iIndex ++;
      if(iIndex == iRealSize){
        iIndex = -1;
        break;
      }
      qFront = multiply(qFront, qReal[iIndex]);
    }
    //cout << "i:" << iIndex;
    if(iIndex == -1) {
      cout << "NO";
      return;
    }
    
    iIndex++;
    qFront = qReal[iIndex];
    while(qFront != QUATERNIONS_j){
      iIndex ++;
      if(iIndex == iRealSize){
        iIndex = -1;
        break;
      }
      qFront = multiply(qFront, qReal[iIndex]);
    }
    //cout << " j:" << iIndex;
    if(iIndex == -1) {
      cout << "NO";
      return;
    }

    iIndex++;
    qFront = qReal[iIndex];
    iIndex ++;
    while(iIndex < iRealSize){
      qFront = multiply(qFront, qReal[iIndex]);
      iIndex ++;
    }
    //cout << " k:" << iIndex << " ";
    if(qFront == QUATERNIONS_k)
      cout << "YES";
    else
      cout << "NO";
  }
  int L;
  unsigned long long X;
  int qInput[10000];
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