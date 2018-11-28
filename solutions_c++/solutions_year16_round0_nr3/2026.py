#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <math.h>
#include <time.h>

struct Test {
  int jam_length;
  int jam_number;
  Test() : jam_length(0), jam_number(0) {}
  Test(int jam_length, int jam_number)
  : jam_length(jam_length), jam_number(jam_number) {}
};

typedef std::vector<bool> Jamcoin;

struct Answer {
  Jamcoin jamcoin;
  std::vector<long> divisors;
  Answer() : jamcoin(Jamcoin(0)), divisors(std::vector<long>(0)) {}
  Answer(Jamcoin &jamcoin, std::vector<long> &divisors)
  : jamcoin(jamcoin), divisors(divisors) {}
};

Jamcoin GenerateRandomJamcoin(int size) {
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<int> distribution(0,1);
  Jamcoin coin(size);
  coin[0] = 1;
  coin[size - 1] = 1;
  for (int i = 1; i < size - 1; ++i) {
    coin[i] = distribution(gen);
  }
  return coin;
}

std::vector<std::vector<int>> GenMaskNumbersForSyst(size_t size, int syst) {
  std::vector<std::vector<int>> base(size, std::vector<int>(size));
  base[0][size - 1] = 1;
  for (size_t i = 1; i < size; ++i) {
    int going_through = 0;
    for (int j = static_cast<int>(size) - 1; j >= 0 ; --j) {
      base[i][j] = (going_through + base[i-1][j] * syst) % 10;
      going_through = (base[i-1][j] * syst + going_through - base[i][j])/10;
    }
  }
  return base;
}

std::vector<int> FromSystToDecimal(Jamcoin &coin, int syst) {
  std::vector<int> decimal(coin.size());
  std::vector<std::vector<int>> base = GenMaskNumbersForSyst(coin.size(), syst);
  for (size_t i = 0; i < coin.size(); ++i) {
    if (coin[i]) {
      int going_through = 0;
      int buf = 0;
      for (int j = static_cast<int>(coin.size()) - 1; j >= 0; --j) {
        buf = decimal[j] + base[coin.size() - 1 - i][j] + going_through;
        decimal[j] = (decimal[j] + base[coin.size() - 1 - i][j] + going_through)%10;
        going_through = (buf - buf%10)/10;
      }
    }
  }
  std::vector<int> result;
  bool flag = false;
  for (size_t i = 0 ; i < decimal.size(); ++i) {
    if (decimal[i] != 0 || flag) {
      flag = true;
      result.push_back(decimal[i]);
    }
  }
  return result;
}

std::vector<int> divide(std::vector<int> vec, long divisor) {
  std::vector<int> result;
  long buf = 0;
  for (size_t i = 0; i < vec.size(); ++i) {
    buf = buf*10 + vec[i];
    if (buf/divisor >= 1) {
      result.push_back(buf/divisor);
      buf = buf%divisor;
    }
  }
  if (buf != 0) {
    return std::vector<int> (1, -1);
  } else {
    return result;
  }
}

std::vector<long> FindDivisors(Jamcoin &coin) {
  std::vector<long> divisors(9);
  for (int i = 0; i < 9; ++i) {
    std::vector<int> decimal_number = FromSystToDecimal(coin, i+2);
    long j;
    for (j = 2; j < pow(10, 3); j++) {
      std::vector<int> res = divide(decimal_number, j);
      if (res[0] != -1) {
        divisors[i] = j;
        break;
      }
    }
    if (j >= pow(10, 3)) {
      divisors[0] = -1;
      return divisors;
    }
  }
  return divisors;
}

std::vector<Answer> FindJamcoins(Test test) {
  std::vector<Answer> jamcoins(test.jam_number);
  for (int i = 0; i < test.jam_number; ++i) {
    Jamcoin buf = GenerateRandomJamcoin(test.jam_length);
    std::vector<long> divisors = FindDivisors(buf);
    while (divisors[0] == -1) {
      buf = GenerateRandomJamcoin(test.jam_length);
      divisors = FindDivisors(buf);
//          for (int j = 0; j < buf.size(); ++j) {
//            std::cout << buf[j];
//          }
//          std::cout << "lawl\n";
    }
    jamcoins[i].jamcoin = buf;
    jamcoins[i].divisors = divisors;
  }
  return jamcoins;
}

int main() {
  int test_number;
  std::cin >> test_number;
  std::vector<Test> tests(test_number);
  for (int i = 0; i < test_number; ++i) {
    std::cin >> tests[i].jam_length >> tests[i].jam_number;
  }
  for (int i = 0; i < test_number; ++i) {
    std::cout << "Case #" << i + 1 << ":\n";
    std::vector<Answer> jamcoins = FindJamcoins(tests[i]);
    
    for (int index = 0; index < jamcoins.size(); ++index) {
      for (int j = 0; j < jamcoins[index].jamcoin.size(); ++j) {
        std::cout << jamcoins[index].jamcoin[j];
      }
      std::cout << ' ';
      for (int j = 0; j < jamcoins[index].divisors.size(); ++j) {
        std::cout << jamcoins[index].divisors[j] << ' ';
      }
      std::cout << '\n';
    }
  }
//  std::vector<std::vector<int>> base = GenMaskNumbersForSyst(6, 8);
//  for (int i = 0; i < base.size(); ++i) {
//    for (int j = 0; j < base.size(); ++j) {
//      std::cout << base[i][j];
//    }
//    std::cout << "\n";
//  }
//  Jamcoin coin(5, 1);
//  std::vector<int> dec = FromSystToDecimal(coin, 8);
//  for (size_t i = 0; i < dec.size(); ++i) {
//    std::cout << dec[i];
//  }
//  std::cout << "\n";
//  std::vector<int> div = divide(dec, 151);
//  for (size_t i = 0; i < div.size(); ++i) {
//    std::cout << div[i];
//  }
//  std::cout << "\n";
  return 0;
}
