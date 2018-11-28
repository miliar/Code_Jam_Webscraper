#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++){
    int res = -1;
    bool nDict[10] = { false };    
    long long out;  
    long long N;
    int r;
    cin >> N;
    for(long long copyN = N; copyN > 0; copyN += N) {
      if (copyN == 0){
        break;
      }
      long long tempN = copyN;
      while (tempN > 0){
        r = tempN % 10;
        tempN = tempN / 10;
        nDict[r]++;
      }
      bool allFilled = true;
      for(int i = 0; i < 10; i++){
        allFilled = allFilled && nDict[i];
      }
      if (allFilled) {
        res = copyN;
        break;
      } 
    }
    cout << "Case #" << t << ": ";
    if (res < 0) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << res << endl;
    }
  }
  return 0;
}