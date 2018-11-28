#include <iostream>
#include <fstream>
#include <vector>

long testTilesFrom(long pos, long c, long k) {
  long abs_pos = 1;

  for (long i = 0; i < c; ++i) {
    abs_pos = k*(abs_pos-1) + pos;
    if (pos < k) ++pos;
  }
  return abs_pos;
}

std::vector<long> solve(long k, long c, long s) {
  if (s * c < k) return {};

  std::vector<long> soln;
  
  for (long t = 1; t <= k; t += c) {
    soln.push_back(testTilesFrom(t, c, k));
  }

  return soln;
}

int main(int argc, char* argv[]) {

  if (argc < 3) {
    std::cout << "usage: " << argv[0] << " <infile> <outfile>" << std::endl;
    return 0;
  }

  std::ifstream infile {argv[1]};
  std::ofstream outfile {argv[2]};

  int nCases;
  infile >> nCases;
  infile.ignore(100, '\n');

  for (int caseNum = 1; caseNum <= nCases; ++caseNum) {
    int k, c, s;
    infile >> k >> c >> s;

    outfile << "Case #" << caseNum << ": ";
    
    auto soln = solve(k, c, s);
    if (soln.size() == 0) {
      outfile << "IMPOSSIBLE";
    } else {
      for (auto& x : soln) {
        outfile << x << " ";
      }
    }
    
    outfile << std::endl;
  }
}

