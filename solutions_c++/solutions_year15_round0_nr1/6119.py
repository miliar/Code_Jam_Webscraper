#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <algorithm>
#include "print_routines.h"

template<typename Type>
std::string Str(const Type& v) {
  std::ostringstream stream;

  stream << v;
  return stream.str();
}

template<typename T>
T FromString(const std::string& s) {
  T result;

  std::istringstream stream( s );
  stream >> result;

  return result;
}

/*
int main(int argc, char* argv[]) {
  std::ifstream in("in.txt");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    int result = 0;

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}
*/

int main(int argc, char* argv[]) {
  std::ifstream in("A-large.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    int result = 0;

    int s_max = 0;
    in >> s_max;

    std::string shyness;
    in >> shyness;

    for (int i = 0; i < shyness.size(); ++i)
      shyness[i] = shyness[i] - '0';

    int sum = shyness[0];
    for (int i = 1; i < shyness.size(); ++i) {
      if (sum < i) {
        int invite = i - sum;
        result += invite;
        sum += (invite + shyness[i]);
      } else {
        sum += shyness[i];
      }
    }

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}