#include <iostream>
#include <vector>
#include <algorithm>

int solve(const std::vector<double> &l1, const std::vector<double> &l2);
std::vector<double> loadBlocks(int size);

int main() {
  std::vector<double> l1, l2;
  int n;
  int blockCnt;
  int legitCnt, cheatCnt;
  double tmp;
  std::cin >> n;

  for(int i=1; i<=n; i++) {
    std::cin >> blockCnt;
    l1 = loadBlocks(blockCnt);
    l2 = loadBlocks(blockCnt);
    legitCnt = solve(l1, l2);
    cheatCnt = solve(l2, l1);
    cheatCnt = blockCnt - cheatCnt;
    std::cout << "Case #" << i << ": " << cheatCnt << " " << legitCnt << std::endl;
  }

  return 0;
}

std::vector<double> loadBlocks(int size) {
  std::vector<double> blocks;
  double tmp;

  for(int i=0; i<size; i++) {
    std::cin >> tmp;
    blocks.push_back(tmp);
  }
  std::sort(blocks.begin(), blocks.end());
  return blocks;
}

int solve(const std::vector<double> &l1, const std::vector<double> &l2) {
  int value = 0;
  int l1Front, l1End, l2Front, l2End;
  l1Front = l2Front = 0;
  l1End = l2End = l1.size()-1;

  for(int i=0; i<l1.size(); i++) {
    if(l1[l1End] > l2[l2End]) {
      l1End--;
      l2Front++;
      value++;
    } else {
      l1End--;
      l2End--;
    }
  }

  return value;
}
