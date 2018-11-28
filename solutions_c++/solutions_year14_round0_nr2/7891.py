#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
  ifstream fin("B-small-attempt0.in");
  ofstream fout("B-small-attempt0.out");
  int T;
  double get, sum, spend, extra, target;
  double time_farm, time_win;
  fin >> T;
  for (int account = 1; account <= T; account++) {
    fin >> spend >> extra >> target;
    sum = 0;
    get = 2;
    while (1) {
      time_win = target / get;
      double time_get_farm = spend / get,
             time_then_win = target / (get + extra);
      time_farm =  time_get_farm + time_then_win;
      if (time_win <= time_farm) {
        sum += time_win;
        break;
      }
      sum += time_get_farm;
      get += extra;
    }
    fout << "Case #" << account << ": ";
    fout << setiosflags(ios::fixed) << setprecision(7)
         << sum << endl;
  }
}

