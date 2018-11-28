// Infinite House of Pancakes
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>

typedef std::map<std::string, int> TableType;



std::string vectorToStr (const std::vector<int>& v) {
  std::stringstream result;
  for (int i = 0; i < v.size(); ++i) {
    result << v[i] << " " ;
  }
  return result.str();
}

void eat(std::vector<int>& v, int n) {
  for (int i = 0; i < v.size(); ++i) {
    v[i] -= n;
  }
}

int solveImpl(TableType& table, std::vector<int> v, int time) {
  // base case
  if (v.empty()) {
    return time;
  }

  int maxElem = *std::max_element(v.begin(), v.end());
  if (maxElem <= 2)
    return maxElem + time;
  
  // recursive step
  std::sort(v.begin(), v.end());
  
  // variant 1 - eat
  std::vector<int> vEat(v);
  eat(vEat, 1);
  vEat.erase(std::remove(vEat.begin(), vEat.end(),0), vEat.end());
  int eatTime = solveImpl(table, std::move(vEat), time) + 1;
  
  // variant 2 - happy minute
  maxElem = v.back(); v.pop_back();
  int toGive = maxElem & 0x1 ? maxElem / 3 : maxElem / 2;
  int residual = maxElem - toGive;
  v.push_back(toGive);
  v.push_back(residual);
  int splitTime0 = solveImpl(table, v, time + 1);
  
  
  return std::min(eatTime, splitTime0);
}

int solve(TableType& memoizTable, std::vector<int>& v) {
  
  int bestTime = solveImpl(memoizTable, v, 0);

  return bestTime;
}

int main() {
  std::fstream in("D:\\USACO\\USACO\\resources\\B-small-attempt12.in");
  //std::fstream in("D:\\USACO\\USACO\\resources\\in.txt");
  std::fstream out("D:\\USACO\\USACO\\resources\\out.txt");
  int nOfTestCases;

  TableType table; // memoization

  in >> nOfTestCases;
  for (int testCaseId = 1; testCaseId <= nOfTestCases; ++ testCaseId) {
    int nonEmptyDinners;
    in >> nonEmptyDinners;
    std::vector<int> pancakesPerPlate(nonEmptyDinners);
    for (int plate = 0; plate < nonEmptyDinners; ++plate) {
      in >> pancakesPerPlate[plate];
    }
    out << "Case #" << testCaseId << ": " << solve(table, pancakesPerPlate) << std::endl;
  }
  in.close();
  out.close();

  return 0;
}