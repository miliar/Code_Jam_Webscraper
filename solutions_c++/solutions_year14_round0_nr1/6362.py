#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

#include "tools.hpp"

const int PROBLEM_LENGTH = 10;
const int NUM_ROWS = 4;

void SolveProblem(std::vector<std::string> &problem, int problem_number) {
  int first_row_index = std::stoi(problem[0]);
  int second_row_index = std::stoi(problem[5]);

  std::vector<std::string> first_row = SplitString(problem[first_row_index], ' ');
  std::vector<std::string> second_row = SplitString(problem[5 + second_row_index], ' ');

  int match_count = 0;
  std::string match;

  for (int i = 0, len = first_row.size(); i < len; ++i) {
    if (VectorContains<std::string>(second_row, first_row[i])) {
      ++match_count;
      match = first_row[i];
    }
  }

  std::cout << "Case #" << (problem_number + 1) << ": ";
  if (match_count == 0) {
    std::cout << "Volunteer Cheated!";
  } else if (match_count == 1) {
    std::cout << match;
  } else if (match_count > 1) {
    std::cout << "Bad magician!";
  }

  std::cout << std::endl;
}

int main(int argc, char **argv) {
  if (argc <= 1) {
    std::cout << "USAGE: magic_trick <input file>" << std::endl;
    return 0;
  }

  std::string contents = ReadFile(argv[1]);
  std::vector<std::string> lines = SplitString(contents, '\n');

  int problem_count = std::stoi(lines[0]);
  std::vector<std::string> problem;
  int cur_loc = 1;

  for (int i = 0; i < problem_count; ++i) {
    problem.clear();
    for (int j = 0; j < PROBLEM_LENGTH; ++j) {
      problem.push_back(lines[cur_loc++]);
    }
    SolveProblem(problem, i);
  }

  return 0;
}