#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<string> GetInput()
{
  int testCases;
  cin >> testCases;
  // cout << "Testcases = " << testCases << "\n";
  vector<string> cases;
  for (int i = 0; i < testCases; i++) {
    std::string test;
    cin >> test;
    cases.push_back(test);
  }
  return cases;
}

void print(vector<bool> cakes, uint64_t size) {
  for (size_t i = 0; i < size; i++) {
    std::cout << cakes[i] << " ";
  }
  std::cout << "\n";
}


bool IsDone(vector<bool> cakes)
{
  std::all_of(cakes.begin(), cakes.end(), [](bool cake) { return cake; });
}

void Flip(vector<bool> &cakes, uint64_t count) {
  if (count == 1) {
    cakes[0] = !cakes[0];
    return;
  }
  vector<bool> temp = cakes;

  for (uint64_t i = 0; i < count; i++) {
    temp[i] = !cakes[count - i - 1];
  }
  cakes = temp;
}

uint64_t HappyFaceUp(vector<bool> &cakes, uint64_t downIndex) {
  // Find the index of last +
  uint64_t lastPIndex = 0;
  for (; lastPIndex < downIndex; lastPIndex++) {
    if (!cakes[lastPIndex]) { break; }
  }
  if (lastPIndex == 0) {
    // cout << "Flipping at " << downIndex << ": ";
    // print(cakes, downIndex + 1);
    Flip(cakes, downIndex + 1);
    return 1;
  }
  // cout << "Flipping at " << lastPIndex - 1 << ": ";
  // print(cakes, lastPIndex);
  Flip(cakes, lastPIndex);

  // cout << "Flipping at " << downIndex << ": ";
  // print(cakes, downIndex + 1);
  Flip(cakes, downIndex + 1);
  return 2;
}

uint64_t findIndex(const vector<bool> &cakes) {
  uint64_t index = 0;
  bool start = false;
  for(; index < cakes.size(); index ++) {
    if (!cakes[index] && !start) start = true;
    if (cakes[index] && start) {
      return index - 1;
    }
  }
  return (start) ? index - 1 : index;
}

uint64_t MinFlips(string input)
{
  vector<bool> cakes;
  std::for_each(input.begin(), input.end(), [&cakes](char str) { cakes.push_back((str == '+') ? 1 : 0);});

  // std::for_each(cakes.begin(), cakes.end(), [](bool i) { cout << (int)i; });
  // cout << "\n";

  uint64_t flips = 0;
  while (!IsDone(cakes)) {
    // find first -
    auto index = findIndex(cakes);
    if (index == cakes.size()) {
      return flips;
    }
    flips += HappyFaceUp(cakes, index);
  }
  return flips;
}


int main(int argc, char *argv[])
{
  vector<string> testCases;
  try {
    testCases = GetInput();
  }
  catch (...) {
    cout << "Unable to get testcases\n";
    return 1;
  }
  int index = 1;
  std::for_each(testCases.begin(), testCases.end(), [&index](string testCase) { 
      std::cout << "Case #" << index++ << ": " << MinFlips(testCase) << "\n";
      // std::cout << testCase << " => ";
      // MinFlips(testCase);
    });
  return 0;
 
  /*
  std::string input = argv[1];
  auto flips = MinFlips(input);
  std::cout << "MinFlips = " << flips << "\n";
  return 0;
  */
}
