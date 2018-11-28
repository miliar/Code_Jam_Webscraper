#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <list>
 
using namespace std;
 
class qb {
 public:
  qb() {
  }

  ostringstream convert;

  double get_dur(double cur, double regen) {
    double dont_buy = (X-cur)/regen;
    double buy = (C-cur)/regen + X/(regen+F);

    if (dont_buy < buy)
      return dont_buy;
    else
      return (C-cur)/regen + get_dur(0, regen+F);
  }

  string solve() {
    double rate = 2.0;
    double dur = get_dur(0, rate);
    convert << fixed << setprecision(7) << dur;
    return convert.str();
  }

  double C, F, X;

};
 
int main (void) {
  int n, T;

  cin >> T;

  for (n=1; n<=T; n++) {  
    qb *solver = new qb();
    cin >> solver->C >> solver->F >> solver->X;
    cout << "Case #" << n << ": " << solver->solve() << endl;
  }

  return 0;
}
