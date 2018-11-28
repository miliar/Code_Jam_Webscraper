// Standing ovation
#include <fstream>
#include <string>
#include <sstream>

size_t solve(const std::string& Sstr) {
  if (Sstr.empty())
    return 0;
  bool isEmptyLayers = false;
  size_t lastEmptyLayerIndex = 0;
  const size_t nOfLayers = Sstr.size();
  for (int layer = nOfLayers - 1; layer >= 0; --layer) {
    if ('0' == Sstr[layer]) {
      isEmptyLayers = true;
      lastEmptyLayerIndex = layer;
      break;
    }
  }
  if (!isEmptyLayers) return 0;

  int friendsNeeded = 0;
  int nOfPeople = 0;
  for (int layer = 0; layer <= lastEmptyLayerIndex; ++layer) {
    if ('0' == Sstr[layer] && '0' != Sstr[layer + 1]) {
      friendsNeeded += std::max(layer + 1 - nOfPeople - friendsNeeded, 0);
    }
    else if ('0' != Sstr[layer]) {
      char ch = Sstr[layer];
      int peopleOnLayer = std::atoi(&ch);
      nOfPeople += peopleOnLayer;
    }
  }
  return friendsNeeded;
}

int main() {
  std::fstream in("D:\\USACO\\USACO\\resources\\A-large.in");
  std::fstream out("D:\\USACO\\USACO\\resources\\out.txt");
  size_t nOfTestCases;
  
  in >> nOfTestCases;
  for (size_t testCaseId = 1; testCaseId <= nOfTestCases; ++ testCaseId) {
    int Smax;
    std::string Sstr;
    in >> Smax >> Sstr;
    out << "Case #" << testCaseId << ": " << solve(Sstr) << std::endl;
  }
  out.close();
  
  return 0;
}