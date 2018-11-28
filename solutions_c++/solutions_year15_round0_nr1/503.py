#include <iostream>
#include <string>

using namespace std;

class Solver
{
public:
  Solver(){}
  void getInput(){
    cin >> S;
    cin >> k;
  }
  void solve(){
    int *iAudienceArray = new int[k.size()];
    for(int i = 0; i < k.size(); i ++){
      iAudienceArray[i] = k[i] - '0';
    }
    int iInitialCount = 0;
    int iSum = iAudienceArray[0];
    for(int i = 1; i < k.size(); i ++){
      if(iSum + iInitialCount < i)
        iInitialCount = i - iSum;
      iSum += iAudienceArray[i];
    }
    cout << iInitialCount;
  }
  int S;
  string k;
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