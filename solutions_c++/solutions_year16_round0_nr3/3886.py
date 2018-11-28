#include <algorithm>
#include <atomic>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <thread>
#include <mutex>

using namespace std;

void GetInput(int &n, int &j)
{
  int testCases;
  cin >> testCases;
  cin >> n;
  cin >> j;
  return;
}

bool IsPrime(uint64_t i, uint64_t &divisor) {
  if (i == 2 || i == 3) {
    return true;
  }
  if ( (i % 2) == 0 ) {
    divisor = 2;
    return false;
  }
  if ( (i % 3) == 0 ) {
    divisor = 3;
    return false;
  }

  uint64_t val = 5;
  uint64_t inc = 2;
  while ((val * val) <= i) {
    if ((i % val) == 0) {
      divisor = val;
      return false;
    }
    val += inc;
    inc = 6 - inc;
  }
  return true;
}

bool IsPrime1(uint64_t i, uint64_t &divisor)
{
  if (i <= 1) return true;
  for (uint64_t j = 2; j < i; j++) {
    if (i % j == 0) {
      divisor = j;
      return false;
    }
  }
  return true;
}

std::string GetBinary(uint64_t i)
{
  std::string str = "";
  for(uint64_t j = 1; j <= i; j <<= 1) {
    str += ((j & i) > 0) ? "1" : "0";
  }
  std::reverse(str.begin(), str.end());
  return str;
}

uint64_t Convert(uint64_t i, int base)
{
  uint64_t result = 0;
  for (uint64_t j = 1, k = 0; j <= i; j <<= 1, k++) {
    if ((j & i) > 0) {
      // cout << "|" << base << "^" << k;
      result += (uint64_t) std::pow(base, k);
    }
  }
  // std::cout << "\n";
  return result;
}

bool IsJamCoin(uint64_t i, vector<uint64_t> &divisors)
{
  divisors.clear();
  if ((i & 1) == 0) return false;
  for (int j = 2; j < 11; j++) {
    auto value = Convert(i, j);
    uint64_t divisor;
    if (IsPrime(value, divisor)) return false;
    divisors.push_back(divisor);
  }
  return true;
}

class JamCoinPrinter
{
private:
  std::mutex m;
  int size_n;
  int max;
  std::atomic<bool> flag;
public:
  struct JamCoin
  {
    std::string coin;
    std::vector<uint64_t> divisors;
  };
  std::vector<JamCoin> coins;

  JamCoinPrinter(int n, int j) : size_n(n), max(j), flag(false) {}

  // both inclusive
  void Process(uint64_t start, uint64_t end) {
    {
      std::lock_guard<std::mutex> lg(m);
      // std::cout << "Starting process for (" << start << "," << end << ")\n";
    }

    int count = 0;
    std::vector<uint64_t> divisors;
    for (uint64_t iter = start; iter <= end; iter++) {
      
	if (flag.load(std::memory_order_acquire)) {
	  return;
	}

      if (IsJamCoin(iter, divisors)) {
	auto str = GetBinary(iter);
	if (str.size() != size_n) {
	  continue;
	}
	{
	  std::lock_guard<std::mutex> lg(m);
	  if (coins.size() >= max) {
	    flag.store(true, std::memory_order_release);
	    return;
	  }
	  JamCoin jc{GetBinary(iter), divisors};
	  coins.push_back(jc);
	  if (coins.size() >= max)
	    flag.store(true, std::memory_order_release);
	  // std::cout << "Adding coin(" << start << "): " << jc.coin << "\n";
	}
	divisors.clear();
      }
    }  
    // std::cout << "Done: " << start << "|" << end << "\n";  
  }

  void Print() {
    for (size_t i = 0; i < coins.size(); i++) {
      cout << coins[i].coin << " ";
      std::for_each(coins[i].divisors.begin(), coins[i].divisors.end(), [](uint64_t div) { cout << div << " ";});
      cout << "\n";
    }
  }

  void Start(int partitions) {
    uint64_t maxValue = (uint64_t)(1ULL << size_n) - 1;
    uint64_t startValue = (uint64_t)(1ULL << (size_n - 1));
    // cout << size_n << "|" << startValue << "|" << maxValue << "\n";
    uint64_t range = maxValue - startValue + 1;
    std::vector<std::thread> threads;
    uint64_t start = startValue;
    for (int i = 0; i < partitions; i++) {      
      uint64_t end = start + (uint64_t) std::floor(range / partitions) - 1;
      if (end > maxValue)
	end = maxValue;
      if (end > start)
	threads.push_back(std::thread(&JamCoinPrinter::Process, this, start, end));
      start = end + 1;
    }
    for (auto &th : threads) {
      if (th.joinable()) 
	th.join();
    }

    Print();
  }
};

void PrintJamCoins(int n, int j)
{
  uint64_t maxValue = (1 << n) - 1;
  int count = 0;
  std::vector<uint64_t> divisors;
  for (uint64_t iter = 1 << (n-1); iter <= maxValue && count < j; iter++) {
    if (IsJamCoin(iter, divisors)) {
      auto str = GetBinary(iter);
      if (str.size() != n) {
	continue;
      }
      cout << iter << "|" << GetBinary(iter) << " ";
      std::for_each(divisors.begin(), divisors.end(), [](uint64_t value) { cout << value << " "; });
      cout << "\n";
      count++;
      divisors.clear();
    }
  }
}

int main(int argc, char *argv[])
{
  int n, j;
  // GetInput(n, j);

  n = std::stoi(argv[1]);
  j = std::stoi(argv[2]);
  // cout << "N=" << n << "|J=" << j << "\n";
  std::cout << "Case #1:\n";
  JamCoinPrinter printer(n, j);
  printer.Start((n <= 16) ? 1 : 6);
  return 0;

  // int i = std::stoi(argv[1]);
  // int base = std::stoi(argv[2]);
  // std::cout << i << " in base " << base << " (" << GetBinary(i) << ") is " << Convert(i, base) << "\n";

  // uint64_t div;
  // std::cout << i << " is ";
  // if (IsPrime(i, div)) {
  //   cout << "prime";
  // } else {
  //     cout << "not prime with divisor " << div;
  // }
  // cout << "\n";
  return 0;
}
