#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<uint64_t> GetInput()
{
  int testCases;
  cin >> testCases;
  // cout << "Testcases = " << testCases << "\n";
  vector<uint64_t> cases;
  for (int i = 0; i < testCases; i++) {
    uint64_t test;
    cin >> test;
    cases.push_back(test);
  }
  return cases;
}

unordered_set<int> GetDigits(uint64_t num)
{
  unordered_set<int> digits;
  if (num == 0) {
    digits.insert(0);
    return digits;
  }
  for (; num > 0; num /= 10) {
    digits.insert(num % 10);
  }
  return digits;
}

bool CountSheep(uint64_t startNum, uint64_t &output)
{
  if (startNum == 0) {
    return false;
  }
  unordered_set<int> allDigits {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  std::unordered_set<int> digitsSet;
  bool found = false;
  output = startNum;
  for (uint64_t i = 1; !found; i++) {
    output = startNum * i;
    auto digits = GetDigits(output);
    digitsSet.insert(digits.begin(), digits.end());
    found = std::all_of(allDigits.begin(), allDigits.end(), [&digitsSet](int d) { return digitsSet.find(d) != digitsSet.end(); });
    if (i >= 1e9) {
      return false;
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  vector<uint64_t> testCases;
  try {
    testCases = GetInput();
  }
  catch (...) {
    cout << "Unable to get testcases\n";
    return 1;
  }
  int index = 1;
  std::for_each(testCases.begin(), testCases.end(), [&index](uint64_t testCase) { 
      uint64_t output;
      if (CountSheep(testCase, output)) {
	std::cout << "Case #" << index++ << ": " << output << "\n";
      }
      else {
	std::cout << "Case #" << index++ << ": INSOMNIA\n";
      }
    });
  return 0;
}
