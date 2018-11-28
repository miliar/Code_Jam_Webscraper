#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <climits>
using namespace std;

int min_ancestor(const int & P, const int & Q, bool & flag);

int main(int argc, char *argv[]) {
  ifstream in("A-small-attempt3.in");
  if (!in.is_open())
    std::cout << "error opening file in" << std::endl;
  ofstream out("test_output");
  if (!out.is_open())
    std::cout << "error opening file out" << std::endl;
  
  unsigned test_count = 0;
  in >> test_count;
  for (unsigned test_index = 1; test_index <= test_count; ++test_index) {
    int P = 0;
    int Q = 0;
    in >> P;
    in.get();
    in >> Q;
    std::cout << test_index << " " << P << " " << Q << std::endl;

    unsigned q = Q;
    while (q % 2 == 0)
      q /= 2;
    if (q != 1) {
      out << "Case #" << test_index << ": impossible" << std::endl;
      continue;
    }

    int counter = 0;
    while (P < Q) {
      ++counter;
      P *= 2;
    }
    
    if (counter > 40) 
      out << "Case #" << test_index << ": impossible" << std::endl;
    else 
      out << "Case #" << test_index << ": " << counter << std::endl;

  }
  return 0;
}
