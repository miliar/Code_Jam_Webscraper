#include <iostream>
#include <cmath>

using namespace std;

#define _USE_MATH_DEFINES

int main(int argc, char** argv) {

  int T  = 0;
  cin >> T;
    for (int i = 0; i < T; i++) {
 
    long long r = 0;
    cin >> r;    
    long long t = 0;
    cin >> t;
    long long num = 0;

    while (t > 0) {
//      cout << "t: " << t << endl;
//      t -= (pow((r + 1),2) - pow(r,2));
      t -= 2*r + 1;
      r += 2;
      if (t >= 0) {
        num++;
      }
    }

    cout << "Case #" << (i+1) << ": " << num << endl;
  }
}
