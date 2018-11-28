#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <tuple>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <sstream>

typedef unsigned int u32;
typedef unsigned long long u64;

typedef std::tuple<u32, u32> TTuple;

template<typename T>
void HashCombine(std::size_t& aSeed, const T& aValue) {
  aSeed ^= std::hash<T>()(aValue) + 0x9e3779b9 + (aSeed << 6) + (aSeed >> 2);
}
namespace std {
  template<>
  struct hash<TTuple> {
    size_t operator()(const TTuple& aTuple) const {
      size_t hash = 0;
      HashCombine(hash, get<0>(aTuple));
      HashCombine(hash, get<1>(aTuple));
      return hash;
    }
  };
}

struct CProblem {
  std::vector<int> sizes;
  int capacity;
};

struct CResult {
  int CD;
};

CResult Solve(CProblem aProblem) {
  CResult rtn;
  std::sort(aProblem.sizes.begin(), aProblem.sizes.end());
  std::reverse(aProblem.sizes.begin(), aProblem.sizes.end());
  int CD = 0;
  std::vector<bool> taken(aProblem.sizes.size(), 0);
  for (int i=0; i<(int)aProblem.sizes.size(); i++) {
    if (taken[i])
      continue;
    CD++;
    taken[i] = 1;
    for (int j=i+1; j<(int)aProblem.sizes.size(); j++) {
      if (taken[j])
        continue;
      if (aProblem.sizes[i]+aProblem.sizes[j]<=aProblem.capacity) {
        taken[j] = 1;
        std::cerr << aProblem.sizes[i] << " " << aProblem.sizes[j] << "\n";
        break;
      }
    }
  }
  rtn.CD = CD;
  return rtn;
}


int main(int argc, char* argv[]) {
  //const std::string KFileName = "test.txt";
  //const std::string KFileName = "A-small-attempt1.in";
  const std::string KFileName = "A-large.in";

  std::ifstream ifs(KFileName);
  assert(ifs);


  u32 T;
  ifs >> T;
  std::string D;
  std::getline(ifs, D);

  for (u32 i=0; i<T; i++) {
    CProblem problem;
    int N;
    ifs >> N >> problem.capacity;
    problem.sizes.resize(N);
    for (int j = 0; j < N; ++j) {
      ifs >> problem.sizes[j];
    }

    std::cerr << "Solving Problem " << i << "\n";
    const CResult result = Solve(problem);
    std::cout << "Case #" << i+1 << ": ";
   
    std::cout << result.CD << "\n";
  }
}
