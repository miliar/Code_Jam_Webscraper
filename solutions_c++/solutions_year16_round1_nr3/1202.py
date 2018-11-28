//*****************************************************************************
// CodePro 1.0.1 - Programming contests library.
// (C) 2015-2016, Bird of Prey Studio
//     Dr. Sergey Pogodin < dr.pogodin@gmail.com >

enum IOBinding { File, StdStream };

static const IOBinding InputBinding = File;
//static const IOBinding InputBinding = StdStream;

static const IOBinding OutputBinding = File;
//static const IOBinding OutputBinding = StdStream;

enum IOHandlingFlag {
  MultipleTestCases = 0x1,
  PrintCaseNumberInCodeJamStyle = 0x2
};

static const int IOHandlingFlags =
    MultipleTestCases | PrintCaseNumberInCodeJamStyle;

#include <cmath>
#include <cassert>
#include <climits>
#include <cstdint>
#include <cstring>
#include <string>

#include <fstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

typedef std::vector <int> IVec;
typedef std::unordered_set <int> ISet;

std::istream *input = &std::cin;
std::ostream *output = &std::cout;

//*****************************************************************************

class Problem {
public:
  Problem();
  ~Problem();
  void Solve();

private:
  bool good(bool &good_inside);
  void solve();

  int res_;
  int N_;
  IVec best_, state_;
  ISet used_;
};

Problem::Problem() {
  *input >> N_;
  best_.resize(N_);
  for (int n = 0; n < N_; ++n) {
    *input >> best_[n];
    --best_[n];
    //*output << state_[n] << ' ';
  }
//  /*output << '\n';
}

Problem::~Problem() {
}

void Problem::Solve() {
  res_ = 0; solve();
  *output << res_ << '\n';
}

bool Problem::good(bool &good_inside) {
  good_inside = true;
  if (state_.size() == 1) return true;
  else if (state_.size() == 2)
    return (state_.front() == best_[state_.back()]) &&
           (state_.back() == best_[state_.front()]);
  else {
    bool res = (state_.back() == best_[state_.front()])
            || (state_[1] == best_[state_.front()]);
    res &= (state_.front() == best_[state_.back()]) ||
           (state_[state_.size() - 2] == best_[state_.back()]);
    for (int i = 1; i < state_.size() - 1; ++i) {
      good_inside &= (state_[i-1] == best_[state_[i]]) ||
                     (state_[i+1] == best_[state_[i]]);
      if (!good_inside) break;
    }
    res &= good_inside;
    return res;
  }
}

void Problem::solve() {
  if (state_.size() == N_) return;
  for (int i = 0; i < N_; ++i) {
    if (!used_.count(i)) {
      used_.insert(i);
      state_.push_back(i);
      bool good_inside;
      if (good(good_inside)) {
        if (res_ < state_.size()) res_ = state_.size();
      }
      if(good_inside)solve();
      state_.pop_back();
      used_.erase(i);
    }
  }
}

//*****************************************************************************

void InitIOStreams() {
  std::ios_base::sync_with_stdio(false);
  if (InputBinding == File) input = new std::ifstream("input.txt");
  if (OutputBinding == File) output = new std::ofstream("output.txt");
}

void DeinitIOStreams() {
  if (InputBinding == File) delete input;
  if (OutputBinding == File) delete output;
}

int main(int argc, char *argv[]) {
  (void) argc;
  (void) argv;
  InitIOStreams();
  int num_test_cases = 1;
  if (IOHandlingFlags & MultipleTestCases) *input >> num_test_cases;
  for(int t = 1; t <= num_test_cases; ++t) {
    if (IOHandlingFlags & PrintCaseNumberInCodeJamStyle)
      *output << "Case #" << t << ": ";
    Problem *p = new Problem;
    p->Solve(); delete p;
  }
  DeinitIOStreams();
  return 0;
}
