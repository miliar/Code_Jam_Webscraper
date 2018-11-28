#include <iostream>
#include <iomanip>

using namespace std;

double countEffort(double C, double F, double X, int nof) {
  double result = 0;

  for (int i = 0; i < nof; ++i)
    result += C/(2+i*F);

  result += X / (2+nof*F);

  return result;
}

int main() {
  int T;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    double result = 0;
    double C, F, X;
    double cps = 2;

    cin >> C >> F >> X;

    int nof = 1; // number of farms
    double prev = countEffort(C,F,X,0);
    double current = countEffort(C,F,X,1);
    while (prev > current) {
 //     cout << prev << " " << current << endl;
      prev = current;
      current = countEffort(C,F,X,++nof);
    }

    result = prev;
    cout << "Case #" << test << ": " << fixed << setprecision(7) << result << endl;
  }

}
