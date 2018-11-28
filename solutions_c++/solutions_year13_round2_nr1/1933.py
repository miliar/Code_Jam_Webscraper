#include <thread>
#include <future>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <array>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <functional>


// sort input
// iterate over input
// if head smaller then increase self by head
// else add to self (self-1)

using namespace std;

struct Case {
  int number;
  uint64_t mote;
  vector<uint64_t> others;
};

ostream& operator << (ostream& os, const Case& c) {
  os << c.number << " [ mote:" << c.mote << ", others:";
  for(auto a: c.others) {
    os << a << " ";
  }
  os << "]";
  return os;
}

Case readCase(const int number) {
  Case ret;
  ret.number = number;
  cin >> ret.mote;
  uint64_t othersSize;
  cin >> othersSize;
  while(othersSize--) {
    uint64_t other;
    cin >> other;
    ret.others.push_back(other);
  }
  sort(ret.others.begin(),ret.others.end());
  return ret;
}

struct Grow {
  uint64_t mote;
  uint64_t moves = 0;
};

Grow growMinumum(uint64_t currentMote, const uint64_t target) {
  Grow g;
  while(currentMote <= target) {
    g.moves++;
    currentMote += currentMote-1;
  }
  g.mote = currentMote;
  return g;
}

uint64_t solve(const Case& c) {
  if(c.mote == 1)
    return c.others.size();
  uint64_t mote = c.mote;
  uint64_t moves = 0;
  for(int i = 0; i < c.others.size(); ++i) {
    auto other = c.others[i];
    if(other < mote) {
      mote += other;
    } else {
      Case skip;
      copy(c.others.begin()+i+1,c.others.end(), back_inserter(skip.others));
      skip.mote = mote;
      auto movesWithSkip = moves + solve(skip) + 1;

      Grow g = growMinumum(mote,other);
      Case grow;
      copy(c.others.begin()+1+i,c.others.end(), back_inserter(grow.others));
      grow.mote = g.mote + other;
      auto movesWithGrow = g.moves + solve(grow);
      return min(movesWithSkip, movesWithGrow);
    }
  }
  return moves;
}

int main() {
  int T;
  cin >> T;
  vector<Case> cases;
  for(int i = 0; i < T; ++i) {
    cases.push_back(readCase(i));
    // uint64_t moves = solve(c);
    // cout << "Case #" << i+1 << ": " << moves << endl;
  }
  vector<future<uint64_t>> results;
  for(auto c: cases) {
    results.push_back(move(async(launch::async,solve,c)));
  }
  for(int i = 0; i < results.size(); ++i) {
    auto r = results[i].get();
    cout << "Case #" << i+1 << ": " << r << endl;
  }
}
