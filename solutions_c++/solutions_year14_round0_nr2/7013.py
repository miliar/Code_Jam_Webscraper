#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
  setprecision(7);
  ifstream readFile;
  ofstream writeFile;
  readFile.open("qualB_small.txt");
  writeFile.open("solution_qualB_small.txt");

  int numTestCases;
  double C, F, X, time_one, time_two, current_rate, current_cookie_num, total_time;
  readFile >> numTestCases;

  for(int i = 1; i <= numTestCases; i++) {
    readFile >> C >> F >> X;
    current_rate = 2.0;
    total_time = 0;
    time_one = (X)/(current_rate);
    time_two = C/(current_rate) + (X)/(current_rate+ F);
    while(time_one > time_two) {
       total_time += C/current_rate;
       current_rate += F;
       time_one = (X)/(current_rate);
       time_two = C/(current_rate) + (X)/(current_rate+ F);
     } 
    total_time += time_one;
    writeFile.precision(7);
    writeFile << "Case #" << i << ": " << total_time << endl;
  }
  return 0;
}
