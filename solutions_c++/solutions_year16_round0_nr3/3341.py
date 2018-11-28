#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>

unsigned long computeInBase(const std::vector<int> &binary, int base) {
  unsigned long result = 0;
  for (int i = 0; i < binary.size(); i++) {
    result += pow(base, i) * binary[i];
  }
  return result;
}


// returns 0 on failure
unsigned long findDivisor(unsigned long number) {
  float sqrt_num = sqrt(number);
  for (unsigned long i = 2; i < sqrt_num; i++) {
    if (number % i == 0) {
      return i;
    }
  }
  return 0;
}

std::vector<std::vector<int> > generateJamcoins(unsigned int length) {
  std::vector<std::vector<int> > result;
  std::vector<int> jamcoin(length);
  jamcoin[0] = 1;
  jamcoin[length-1] = 1;

  unsigned long combinations = pow(2, length-2);
  for (unsigned long i = 0; i < combinations; i++) {
    for (unsigned int j = 1; j < length - 1; j++) {
      int power = pow(2, (j-1));
      jamcoin[j] = (i / power) % 2;
    }
    result.push_back(jamcoin);
  }  
  return result;
}

void printJamcoin(const std::vector<int> &jamcoin) {
  for (int i = jamcoin.size()-1; i >= 0; i--)
    std::cout << jamcoin[i];
}

int main(int argc, char** argv) {
  unsigned int T;
  unsigned int N;
  unsigned int J;
  std::cin >> T;

  for (int i = 0; i < T; i ++) {
    std::cin >> N;
    std::cin >> J;
    unsigned int num_jamcoins = 0;
    unsigned long divisors[9];

    // number of possible jamcoins is 2^(N-2)
    unsigned int MAX_JAMCOINS = pow(2, N-2);

    if (J > MAX_JAMCOINS) {
      std::cerr << "Asking for the impossible!" << std::endl;
      return -1;
    }

    // generate all possible jamcoins
    std::vector<std::vector<int> > jamcoins = generateJamcoins(N);

    std::cout << "Case #" << i+1 << ":" << std::endl;

    for (int j = 0; j < jamcoins.size() && num_jamcoins < J; j++) {
      bool prime = false;
      // test for divisor in all bases
      for (int k = 2; k <= 10; k++) {
        divisors[k-2] = findDivisor(computeInBase(jamcoins[j], k));
        if (divisors[k-2] == 0) {
          prime = true; 
          break;
        }
      }

      if (!prime) {
        // print jamcoin and it's divisors
        printJamcoin(jamcoins[j]);
        for (int k = 0; k < 9; k++) {
          std::cout << " " << divisors[k];
        }
        std::cout << std::endl;
        num_jamcoins++;
      }
    }
  }

  return 0;
}

