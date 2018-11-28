#include <iostream>
using namespace std;
int main() {
  double C,F,X;
  int cases;
  int case_num = 0;
  cin >> cases;
  while (cases != 0) {
    cin >> C >> F >> X;
    cout.setf(ios::fixed);
    cout.precision(7);
    int j = 1;
    double T1 = 0;
    double T2 = 0;
    double time1 = X / 2;
    double time2 = (C / 2) + (X / (2 + F));
    while (time2 < time1) {
      time1 = time2;
      for (int i = 0; i <= j; i++) T1 += C / (2 + (i * F));
      T2 = X / (2 + ((j + 1) * F));
      time2 = T1 + T2;
      j++;
      T1 = 0;
    }
    case_num++;
    cases--;
    cout << "Case #";
    cout << case_num;
    cout << ": ";
    cout << time1 << endl;
  }
}