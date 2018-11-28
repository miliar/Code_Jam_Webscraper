#include <iostream>
#include <cstring>

using namespace std;

class Solver
{
public:
  Solver(){
    memset(m_iCakesNumberCount, 0, sizeof(m_iCakesNumberCount));
    m_iMaxCount = 0;
  }
  void getInput(){
    cin >> D;
    for(int i = 0; i < D; i++){
      int iInput;
      cin >> iInput;
      if (iInput > m_iMaxCount){
        m_iMaxCount = iInput;
      }
      m_iCakesNumberCount[iInput]++;
    }
  }
  void solve(){
    int iBestCost = m_iMaxCount;
    for(int i = 1; i <= m_iMaxCount; i++){
      int iCost = 0;
      for(int j = i; j <= m_iMaxCount; j++){
        if(m_iCakesNumberCount[j] > 0){
          int iJCost = j/i;
          if (j%i == 0){
            iJCost --;
          }
          iCost += iJCost * m_iCakesNumberCount[j];
        }
      }
      if(iCost + i < iBestCost)
        iBestCost = iCost + i;
    }
    
    cout << iBestCost;
  }
  int D;
  int m_iCakesNumberCount[1001];
  int m_iMaxCount;
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