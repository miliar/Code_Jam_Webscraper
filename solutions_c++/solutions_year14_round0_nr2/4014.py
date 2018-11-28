// Google Code Jam, Qual Round, Problem B

#include <iostream>
#include <stdio.h>

#define INITIALRATE 2
using namespace std;

double time_to_win(double X, double C, double F, double baseRate);

int main() {
  int cases;
  cin >> cases;
  for (int case_num=1; case_num < cases + 1; case_num++) {
    double C, F, X;
    cin >> C; cin >> F; cin >> X; 
    bool done = false;
    int farms = 0;
    double current_time_to_win; 
    double time_to_farm;
    double new_time_to_win;
    double total_time = 0;

    do {
      current_time_to_win = X / (INITIALRATE + F*farms); 
      time_to_farm = C / (INITIALRATE + F* farms);
      new_time_to_win = X / (INITIALRATE + F * (farms + 1));
      if (new_time_to_win + time_to_farm < current_time_to_win) {
        total_time += time_to_farm;
        farms++;
      } else {
        total_time += current_time_to_win;
        done = true;
      }
    } while (!done);
    printf("Case #%d: %.7f\n", case_num, total_time);
  }
}
