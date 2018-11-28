#include <iostream>
#include <fstream>

std::string solve(std::string& n);

int main(int argc, char* argv[]) {

  if (argc < 2) {
    std::cout << "usage: " << argv[0] << " <infile> [<outfile>]" << std::endl;
    return 0;
  }

  std::ifstream infile {argv[1]};
  
  std::ostream* out = &std::cout;
  if (argc > 2) out = new std::ofstream{argv[2]};

  int nCases;
  infile >> nCases;
  infile.ignore(100, '\n');

  for (int caseNum = 1; caseNum <= nCases; ++caseNum) {
    std::string s;
    std::getline(infile, s);

    *out << "Case #" << caseNum << ": " << std::flush;
    *out << solve(s);
    *out << std::endl;
  }

  if (argc > 2) delete out;
}

std::string solve(std::string& s) {
  std::string ans {};
  for (char c : s) {
    if (ans == "" || c >= ans[0]) ans = c + ans;
    else ans += c;
  }
  return ans;
}




