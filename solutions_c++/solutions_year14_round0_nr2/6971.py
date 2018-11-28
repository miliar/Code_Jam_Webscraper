#include <iostream>
#include <iomanip>

#define INF 2000000000

using namespace std;

double timeTo(double cps, double objective) {
  return objective / cps;
}

void solve(int t) {
  double C, F, X; cin >> C >> F >> X;

  double cps = 2;
  double totalTime = 0;
  double lastTime = INF;

  
  while (true) {
    //cout << totalTime + timeTo(farms, C) << endl;
    if (totalTime + timeTo(cps, X) > lastTime) break;

    lastTime = totalTime + timeTo(cps, X);
    totalTime += timeTo(cps, C);

    cps += F;
  }
  
  cout << "Case #" << t << ": " << lastTime << endl;
}

int main() {
  int tc; cin >> tc;
  
  cout << fixed;
  cout << setprecision(8);
    
  for (int i = 1; i <= tc; i++) solve(i);
}
