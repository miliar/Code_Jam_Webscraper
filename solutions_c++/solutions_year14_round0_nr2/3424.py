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
#include "print_routines.h"

template<typename Type>
std::string Str(const Type& v) {
  std::ostringstream stream;

  stream << v;
  return stream.str();
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
  std::ifstream in("B-large.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    double result = 0.0;

    double V = 2.0;

    double C = 0.0;
    in >> C;

    double F = 0.0;
    in >> F;

    double X = 0.0;
    in >> X;

    double t = 0.0;
    while (true) {
      double t1 = X / V;
      double t2 = C / V + X / (V + F);
      if (t1 < t2) {
        t += t1;
        break;
      } else {
        t += C / V;
        V += F;
      }
    }

    result = t;

    out << std::fixed;
    out << std::setprecision(8);

    std::cout << std::fixed;
    std::cout << std::setprecision(8);

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}