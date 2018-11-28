#include <iostream>
#include <vector>
#include <Math.h>
#include <bitset>

unsigned long long getFactor(unsigned long long num) {
  if (num % 2 == 0) {
    return 2;
  }
  unsigned long long limit = floor(sqrt(num));
  unsigned long long factor = 3;
  for(; factor <= limit; factor += 2) {
    if(num % factor == 0) {
      return factor;
    }
  }
  return 0;
}

std::string toBinary(unsigned long long num) {
  std::bitset<16> mybitset{num};
  return mybitset.to_string();
}

long toBase(std::string num, int b) {
  //get to the first 1
  std::string::iterator itr = num.begin();
  while(*itr != '1') {
    ++itr; 
  }
  
  //start count
  long total = 0;
  while(itr != num.end()) {
    if(*itr == '0') {
      total = total*b;
    } else {
      total = total*b + 1;
    }
    ++itr;
  }
  return total;
}

void get_jamcoins(long N, long J) {
  int num = 10001;
  for(int i = 2; i < 11; ++i) {
    //std::cout << toBase(num, i) << "\n";
  }
}

void printBinary(std::string bin) {
  //get to the first 1
  std::string::iterator itr = bin.begin();
  while(*itr != '1') {
    ++itr; 
  }
  while(itr != bin.end()) {
    std::cout << *itr;
    ++itr;
  }
}

void printFactors(std::vector<unsigned long long>& res) {
  for(int i = 0; i < 8; ++i) {
    std::cout << res[i] << " ";
  }
  std::cout << res[8] << "\n";
}

void generate_capped_combinations(int len, int cap) {
  int count = 0;
  for(unsigned long long i = pow(2,len - 1) + 1; i < pow(2, len); i += 2) {
    std::vector<unsigned long long> goodOptions;
    std::string bin = toBinary(i);
    for(int j = 2; j < 11; ++j) {
      unsigned long long tmp = toBase(bin, j);
      unsigned long long fct = getFactor(tmp);
      if(fct != 0) {
        goodOptions.push_back(fct);
      } else {
        break;
      }
    }

    if(goodOptions.size() == 9) {
      printBinary(bin);
      std::cout << " ";
      printFactors(goodOptions);
      ++count;
      if(count == cap) {
        break;
      }
    }
  }

}

int main() {
  std::cout << "Case #1:" << "\n";
  generate_capped_combinations(16, 50);
  return 0;
}

