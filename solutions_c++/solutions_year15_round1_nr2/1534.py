#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int m, int n)
{
  int tmp;
  while(m) { tmp = m; m = n % m; n = tmp; }       
  return n;
}

class Event{
public:
  Event(int iBarber, int iTime){
    m_iBarber = iBarber;
    m_iTime = iTime;
  }
  void decreaseTime(int iTime){
    m_iTime -= iTime;
  }
  int m_iTime;
  int m_iBarber;
};

bool operator<(const Event& x, const Event& y)
{
  if(x.m_iTime == y.m_iTime) return x.m_iBarber > y.m_iBarber;
  else return x.m_iTime > y.m_iTime;
}
class Solver
{
  
public:
  Solver(){}
  void getInput(){
    cin >> B;
    cin >> N;
    M = new int[B];
    for(int i = 0; i < B; i ++){
      cin >> M[i];
    }
  }
  void reduceN(){
    int iLCM = M[0];
    for(int i = 1; i < B; i++){
      if(iLCM % M[i] != 0){
        iLCM *= (M[i]/gcd(iLCM, M[i]));
      }
    }
    int iTotal = 0;
    for(int i = 0; i < B; i++){
      iTotal += iLCM / M[i];
    }
    N = N%iTotal;
    N += iTotal;
  }
  void solve(){
    vector<Event> vEvent;
    if(B == 1){
      cout << 1;
      return;
    }
    reduceN();
    if(N <= B){
      cout << N;
      return;
    }
    vEvent.reserve(B);
    for(int i = 0; i < B; i++){
      Event eventNew(i, M[i]);
      vEvent.push_back(eventNew);
      N--;
    }
    sort(vEvent.begin(), vEvent.end());
    while(N > 1){
      int iDecreaseTime = vEvent.back().m_iTime;
      int iBarber = vEvent.back().m_iBarber;
      vEvent.pop_back();
      Event newEvent(iBarber, M[iBarber]);
      bool bInsert = false;
      for(int i = 0; i < vEvent.size(); i++){
        vEvent[i].decreaseTime(iDecreaseTime);
        if(!bInsert && newEvent < vEvent[i]){
          vEvent.insert(vEvent.begin() + i, newEvent);
          i++;
          bInsert = true;
        }
      }
      if(!bInsert){
        vEvent.insert(vEvent.end(), newEvent);
      }
      N--;
    }
    cout << vEvent.back().m_iBarber+1;
  }
  int B,N;
  int *M;
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