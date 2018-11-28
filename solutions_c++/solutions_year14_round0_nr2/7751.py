#include <fstream>
using namespace std;

int main(){
    ifstream input;
    input.open("input.in");
    ofstream output;
    output.open("output.out");
    output.precision(10);
    int T;
    input >> T;
    for (int j = 1; j <= T; ++j) {
      double C, F, X;
      input >> C;
      input >> F;
      input >> X;
      double t0 = X / 2;
      double t1 = t0;
      int i{0};
      do {
        ++i;
        t0 = t1;
        t1 = t0 + C / (2 + F * (i - 1)) + X / (2 + F * i) -
             X / (2 + F * (i - 1));
      } while (t0 > t1);
      output << "Case #" << j <<": "<< t0 << endl;
   }
    input.close();
    output.close();
}
