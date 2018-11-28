#include <iostream>
#include <vector>
#include <set>


using namespace std;

int main(void) {
  int T, p;
  cin >> T;
  for(int t=1; t <= T; t++) {
    double c, f, x, prod = 2;
    cin >> c >> f >> x;
    double best = 1000000, total = 0;
    
    while(total <= best) {
      best = min(best, total + x / prod);
      total += c/prod;
      prod += f;
    }
    cout.precision(10);
    cout << "Case #" << t << ": " << best << endl;
  }
}