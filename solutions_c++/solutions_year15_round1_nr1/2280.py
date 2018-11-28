// Infinite House of Pancakes
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solve(vector<int>& intervals) {
  stringstream ss;
  size_t N = intervals.size();
  int countFirst = 0;
  int countSecond = 0;
  
  int maxDiff = 0;
  for (size_t i = 0; i < N - 1; ++i) {
    int diff = intervals[i] - intervals[i+1];
    maxDiff = std::max(maxDiff, diff);
  }

  
  for (size_t i = 0; i < N - 1; ++i) {
    if (intervals[i+1] < intervals[i])
      countFirst += intervals[i] - intervals[i + 1];
    countSecond += std::min(intervals[i], maxDiff);
  }
  ss << countFirst << " " << countSecond;
  return ss.str();
}

int main() {
  std::fstream in("D:\\USACO\\USACO\\resources\\A-large.in");
  /*std::fstream in("D:\\USACO\\USACO\\resources\\in.txt");*/
  std::fstream out("D:\\USACO\\USACO\\resources\\out.txt");
  int nOfTestCases;


  in >> nOfTestCases;
  for (int testCaseId = 1; testCaseId <= nOfTestCases; ++ testCaseId) {
    size_t nOfIntervals;
    in >> nOfIntervals;
    vector<int> intervals(nOfIntervals);
    for (size_t i = 0; i < nOfIntervals; ++i) {
      in >> intervals[i];
    }
    out << "Case #" << testCaseId << ": " << solve(intervals) << std::endl;
  }
  in.close();
  out.close();

  return 0;
}