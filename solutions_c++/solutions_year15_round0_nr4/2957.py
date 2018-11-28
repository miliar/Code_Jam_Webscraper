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

/*
int solve_r(const std::vector<int>& plates) {
  int m = 0;
  int mi = 0;
  for (int i = 0; i < plates.size(); ++i) {
    if (m < plates[i]) {
      m = plates[i];
      mi = i;
    }
  }

  if (m == 1)
    return 1;

  std::vector<int> p = plates;
  p[mi] = m / 2;
  p.push_back(m - m/2);

  return std::min(m, solve_r(p) + 1);
}

int main(int argc, char* argv[]) {
  std::ifstream in("B-small-attempt2.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    int result = 0;

    int d = 0;
    in >> d;

    std::vector<int> plates(d);
    for (int i = 0; i < d; ++i) {
      in >> plates[i];
    }

    result = solve_r(plates);

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}
*/

int main(int argc, char* argv[]) {
  std::ifstream in("D-small-attempt2.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    std::string result;

    int X = 0;
    in >> X;

    int R = 0;
    in >> R;

    int C = 0;
    in >> C;

    if (R == 1 && C == 1 ) {
      if (X == 1)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if ((R == 2 && C == 1) || (R == 1 && C == 2)) {
      if (X == 1 || X == 2)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if ((R == 3 && C == 1) || (R == 1 && C == 3)) {
      if (X == 1)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if ((R == 4 && C == 1) || (R == 1 && C == 4)) {
      if (X == 1 || X == 2)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if (R == 2 && C == 2) {
      if (X == 1 || X == 2)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if ((R == 3 && C == 2) || (R == 2 && C == 3)) {
      if (X == 1 || X == 2 || X == 3)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if ((R == 4 && C == 2) || (R == 2 && C == 4)) {
      if (X == 1 || X == 2)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if (R == 3 && C == 3) {
      if (X == 1 || X == 3)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if ((R == 4 && C == 3) || (R == 3 && C == 4)) {
      if (X == 1 || X == 2 || X == 3 || X == 4)
        result = "GABRIEL";
      else
        result = "RICHARD";
    } else if (R == 4 && C == 4) {
      if (X == 1 || X == 2 || X == 4)
        result = "GABRIEL";
      else
        result = "RICHARD";
    }

    if (result.empty()) {
      std::cout << C << ", " << R << std::endl;
    }

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}