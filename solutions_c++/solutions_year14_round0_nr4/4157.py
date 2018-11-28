
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

int solveWar(std::vector<int> naomi, std::vector<int> ken) {
  std::sort(naomi.begin(), naomi.end());
  std::sort(ken.begin(), ken.end());

  int wins = 0;

  while(!naomi.empty()) {
    int n = naomi.back();
    naomi.pop_back();

    bool lost = false;
    for(auto it = ken.begin(); it != ken.end(); it++) {
      if(*it > n) {
        ken.erase(it);
        lost = true;
        break;
      }
    }
    if(!lost) {
      ken.erase(ken.begin());
      wins++;
    }
  }

  return wins;
}

bool naomiWinsAll(const std::vector<int>& naomi, const std::vector<int>& ken) {
  auto naomiIt = naomi.begin();
  auto kenIt = ken.begin();

  while(naomiIt != naomi.end()) {
    if(*naomiIt < *kenIt) {
      return false;
    }
    naomiIt++;
    kenIt++;
  }

  return true;
}

int solveDeceitfulWar(std::vector<int> naomi, std::vector<int> ken) {
  std::sort(naomi.begin(), naomi.end());
  std::sort(ken.begin(), ken.end());

  while(!naomiWinsAll(naomi, ken)) {
    naomi.erase(naomi.begin());
    ken.pop_back();
  }

  return naomi.size();
}

void readValues(std::vector<int>* target, std::string line, int count) {
  std::stringstream lineStream(line);
  std::string item;

  for(int i = 0; i < count; i++) {
    double valFl;
    
    std::getline(lineStream, item, ' ');
    sscanf(item.c_str(), "%lf", &valFl);

    int valInt = (int)((valFl + 0.000005) / 0.00001);

    target->push_back(valInt);
  }
}

int main() {
	std::string line;

	int numTestCases = 0;
	std::getline(std::cin, line);
	sscanf(line.c_str(), "%d", &numTestCases);

	for(int testCase = 0; testCase < numTestCases; testCase++) {
    int t;

    std::getline(std::cin, line);
    sscanf(line.c_str(), "%d", &t);

    std::vector<int> naomi;
    std::getline(std::cin, line);
    readValues(&naomi, line, t);

    std::vector<int> ken;
    std::getline(std::cin, line);
    readValues(&ken, line, t);

    int war = solveWar(naomi, ken);
    int deceitfulWar = solveDeceitfulWar(naomi, ken);

    std::cout << "Case #" << (testCase + 1) << ": " << deceitfulWar << " " << war << std::endl;
  }

  return 0;
}
