#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int Z;
  cin >> Z;
  for (int z=1; z<=Z; ++z) {
    double c, f, x;
    cin >> c >> f >> x;
    int i = 0;
    double cur_t = 0.0;
   /* 
    i = (f * (x - c) - 2 * c) / (2 * f);
    if (i < 0) i = 0;
    for (int k=0; k<i; ++k) {
      cur_t += c / (2 + k * f);
    }
    cur_t += x / (2 + i * f);
    */
    while (true) {
      if (x / (2 + i *f) > c / (2 + i * f) + x / (2 + (i + 1) * f)) {
        cur_t += c / (2 + i * f);
        i++;
      } else {
        cur_t += x / (2 + i * f);
        break;
      }
    }
    cout << setprecision(10);
    cout << "Case #" << z << ": " << cur_t << endl;
  }
  return 0;
}
