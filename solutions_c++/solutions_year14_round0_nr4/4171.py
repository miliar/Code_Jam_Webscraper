#include <iostream>
#include <deque>
#include <algorithm>
#include <iomanip>

int optimal(std::deque<double> naomi, std::deque<double> ken) {
  int nWin = 0;
  while(naomi.size() > 0) {
    double nBlock = naomi.back();
    naomi.pop_back();
    auto it = std::find_if(std::begin(ken), std::end(ken), [=](double v){return v>nBlock;});
    if(it == std::end(ken)) {
      ++nWin;
      ken.pop_front();
    }
    else {
      ken.erase(it);
    }
  }
  return nWin;
}

int cheating(std::deque<double> naomi, std::deque<double> ken) {
  int nWin = 0;
  while(naomi.size() > 0) {
    if(ken.back() == 1.000000) {
      ken.pop_back();
      naomi.pop_front();
    }
    auto it = std::find_if(std::begin(naomi), std::end(naomi), [=](double v){return v>ken.front();});
    if(it != std::end(naomi)) {
      naomi.erase(it);
      ken.pop_front();
      ++nWin;
    }
    else {
      naomi.pop_front();
      ken.pop_back();
    }
  }
  return nWin;
}

int main() {
  int tcs;
  std::cin >> tcs;
  for(int tc=1; tc<=tcs; ++tc) {
    int numBlocks;
    std::cin >> numBlocks;
    std::deque<double> naomiBlocks(numBlocks);
    for(int i=0; i<numBlocks; ++i)
      std::cin >> naomiBlocks[i];
    std::deque<double> kenBlocks(numBlocks);
    for(int i=0; i<numBlocks; ++i)
      std::cin >> kenBlocks[i];
    std::sort(std::begin(naomiBlocks), std::end(naomiBlocks));
    std::sort(std::begin(kenBlocks), std::end(kenBlocks));

    std::cout << "Case #" << tc << ": " << cheating(naomiBlocks, kenBlocks) << " " << optimal(naomiBlocks, kenBlocks) << "\n";
  }
  return 0;
}
