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

  void solve();

  static bool COMPARE(const std::vector <int> &a, const std::vector <int> &b);

  int N_;
  std::vector < std::vector <int> > lists_;
  IVec heights_;

  IVec ids_, res_;
  ISet used_;
};

Problem::Problem()
{
  *input >> N_;
  lists_.resize(2*N_-1);
  for (int i = 0; i < 2*N_-1; ++i) {
    lists_[i].resize(N_);
    for (int n = 0; n < N_; ++n)
      *input >> lists_[i][n];
  }
}

Problem::~Problem() {

}

bool Problem::COMPARE(const std::vector<int> &a, const std::vector<int> &b) {
  for (int i = 0; i < a.size(); ++i)
    if (a[i] > b[i]) return false;
  else return true;
}

void Problem::Solve() {
  std::sort(lists_.begin(), lists_.end(), COMPARE);
  solve();
  for (int i: res_) *output << i << ' ';
  *output << '\n'; output->flush();
}

void Problem::solve() {
  if (ids_.size() == N_) {
    for (int i = 0; i < N_; ++i) {
      int j;
      for (j = 0; j < 2*N_-1; ++j) {
        if (!used_.count(j)) {
          bool good = true;
          for (int k = 0; k < N_; ++k) {
            good &= lists_[j][k] == lists_[ids_[k]][i];
            if (!good) break;
          }
          if (good) {
            used_.insert(j);
            break;
          }
        }
      }
      if (j == 2*N_-1) {
        if (!res_.empty()) {
          used_.clear();
          for (int i: ids_) used_.insert(i);
          res_.clear(); return;
        }
        else {
          for (int k = 0; k < N_; ++k) {
            res_.push_back(lists_[ids_[k]][i]);
          }
        }
      }
    }
    used_.clear();
    for (int i: ids_) used_.insert(i);
  } else {
    for (int i = ids_.empty() ? 0 : 1+ids_.back(); i < 2*N_-1; ++i) {
      if (!used_.count(i)) {
        ids_.push_back(i);
        used_.insert(i);
        solve();
        if (!res_.empty()) return;
        used_.erase(i);
        ids_.pop_back();
      }
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
