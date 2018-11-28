#include <iostream>

using namespace std;

int main() {
  int numProb;
  cin >> numProb;
  cout.precision(12);
  for (int i = 0; i < numProb; i++) {
    float C,F,X;
    cin >> C >> F >> X;

    double timeToPaySelf = C/F;

    bool done = false;

    double curRate = 2;
    double curTime = 0;
    while (!done) {
      bool nextIsWorth = (X-C)/curRate > timeToPaySelf;
      if (nextIsWorth) {
        curTime = curTime + C/curRate;
        curRate += F;
      }
      else {
        double endTime = curTime + (X)/curRate;
        cout << "Case #" << i +1 << ": " << endTime << endl; 
        done = true;
      }
    }
  }
}
