#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    double C, F, X;
    cin >> C >> F >> X;
    double best = -1;
    double lastInc = 0;
    int numCF = 0;
    while (true) {
      double rate = 2 + numCF * F;
      double ne = X / rate + lastInc;
      if (ne < best || best < 0) {
	best = ne;
      } else {
	break;
      }
      lastInc += C / rate;
      numCF++;
    }
    cout << "Case #" << i + 1 << ": ";
    printf("%.7f\n", best);
  }
}
