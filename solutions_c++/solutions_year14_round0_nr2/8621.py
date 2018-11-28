#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

#define DEBUG 0

void PrintAnswer(int case_num, string answer) {
  cout << "Case #" << case_num << ": " << answer << endl;
}

string Cookie_Clicker_Alpha(ifstream &ifs) {
  stringstream answer;

  // read probrem
  double C, F, X;
  ifs >> C >> F >> X;

#if DEBUG
  // debug
  cout << fixed << setprecision(7)
       << C << " " << F << " " << X << endl;
#endif

  // answer
  double total_time = 0.0f;

  total_time = X * 0.5; // X / 2
#if DEBUG
  cout << "total_time[" << 0.0f << "] = " << total_time << endl;
#endif

  if ( X > C ) {
    double total_time_old = total_time;

    double farm_num = 1.0f;
    double bought_farm_cost = 0.0f;
    while(1) {
      bought_farm_cost += C / (2.0f + F * (farm_num - 1));

      total_time = X / (2 + F * farm_num) + bought_farm_cost;
#if DEBUG
      cout << "total_time[" << farm_num << "] = " << total_time << endl;
#endif

      if (total_time_old < total_time) {
        total_time = total_time_old;
        break;
      }

      total_time_old = total_time;
      farm_num += 1.0f;
    }
  }

  answer << fixed
         << setprecision(7)
         << total_time;

  return answer.str();
}

int main(int argc, char *argv[]) {
  ifstream ifs(argv[1]);
  int case_sum = 0;

  ifs >> case_sum;

  for (int i = 1; i <= case_sum; i++) {
    PrintAnswer(i, Cookie_Clicker_Alpha(ifs));
  }
}
