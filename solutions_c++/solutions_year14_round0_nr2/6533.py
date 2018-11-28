#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;
  
  for(int t=0; t<T; t++) {
    double c, f, x;
    cin >> c >> f >> x;

    double prod=2;
    double time=0;
    while(true) {
      if( x/prod > (c/prod) + x/(prod+f) ) {
        time += c/prod;
        prod += f;
      } else {
        time += x/prod;
        break;
      }
    }

    cout << fixed << setprecision(7) << "Case #" << (t+1) << ": " << time << endl;
  }

  return 0;
}
