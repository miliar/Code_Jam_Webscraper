#include <iostream>
#include <iomanip>
#include <ios>
#include <string>
#include <vector>

#include "tools.hpp"

using std::cout;
using std::endl;
using std::string;
using std::vector;

const float COOKIES_PER_SECOND = 2.0f;

void ProcessGame(const string &line) {
  vector<string> data_str = SplitString(line, ' ');
  double per_second = COOKIES_PER_SECOND,
        farm_cost = std::stod(data_str[0]),
        farm_incr = std::stod(data_str[1]),
        goal = std::stod(data_str[2]),
        seconds = 0;
  bool done = false;

  while (!done) {
    double time_to_goal = goal / per_second,
          next_time_to_goal = goal / (per_second + farm_incr),
          time_to_farm = farm_cost / per_second;

    if (time_to_goal < (time_to_farm + next_time_to_goal)) {
      done = true;
      seconds += time_to_goal;
    } else {
      seconds += time_to_farm;
      per_second += farm_incr;
    }
  }

  cout << std::fixed << std::setprecision(7) << seconds;
}

int main(int argc, char **argv) {
  if (argc <= 1) {
    cout << "USAGE: cookie_clicker_alpha <input file>" << endl;
    return 0;
  }

  vector<string> lines = SplitString(ReadFile(argv[1]), '\n');
  int count = std::stoi(lines[0]);
  lines.erase(lines.begin());

  for (int i = 0, len = lines.size(); i < len; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    ProcessGame(lines[i]);
    cout << endl;
  }
}