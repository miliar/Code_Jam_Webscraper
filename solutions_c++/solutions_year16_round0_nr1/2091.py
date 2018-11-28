#include <iostream>
#include <fstream>

long solve(long n);

int main(int argc, char* argv[]) {

  if (argc < 3) {
    std::cout << "usage: " << argv[0] << " <infile> <outfile>" << std::endl;
    return 0;
  }

  std::ifstream infile {argv[1]};
  std::ofstream outfile {argv[2]};

  int nCases;
  infile >> nCases;

  for (int caseNum = 1; caseNum <= nCases; ++caseNum) {
    long n;
    infile >> n;

    long soln = solve(n);
    outfile << "Case #" << caseNum << ": ";
    if (soln < 0) outfile << "INSOMNIA";
    else outfile << soln;
    outfile << std::endl;
  }
}

long solve(long n) {
  if (n == 0) return -1;  

  int nDigitsSeen {0};
  bool digitsSeen[10];

  for (int i = 0; i != 10; ++i) digitsSeen[i] = false;

  long num = n;
  for (; nDigitsSeen != 10; num += n) {
    
    long digitBuffer = num;
    
    
    while (digitBuffer) {
      int d = digitBuffer % 10;
      digitBuffer /= 10;

      if (!digitsSeen[d]) {
        ++nDigitsSeen;
        digitsSeen[d] = true;
      }
    }
  }

  return num - n;
}




