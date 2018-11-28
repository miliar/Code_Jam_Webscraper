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

int nextden(int V, const std::vector<int>& cur_den) {
  std::vector< int > values( V + 1 );

  int D = cur_den.size();
  for (int i = 1; i < 1 << (D + 1); ++i) {
    int v = 0;
    for (int j = 0; j < D; ++j) {
      if (i & (1 << j))
        v += cur_den[ j ];
    }

    if (v > 0 && v <= V)
      values[v] = 1;
  }

  int result = 0;
  for (int i = 1; i <= V; ++i) {
    if (values[i] == 0) {
      result = i;
      break;
    }
  }

  return result;
}

int main(int argc, char* argv[]) {
  std::ifstream in("C-small-attempt0 (1).in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    int result = 0;

    int C = 0;
    in >> C;

    int D = 0;
    in >> D;

    int V = 0;
    in >> V;

    std::vector< int > den( D );
    for (int i = 0; i < D; ++i)
      in >> den[ i ];

    int nd = 0;
    while ((nd = nextden(V, den)) != 0) {
      result += 1;
      den.push_back(nd);
    }

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}