//*****************************************************************************
//  CodePro 1.0 - Programming contests library.
//
//  (c) Dr. Sergey Pogodin, 2015
//      Contact: dr.pogodin@gmail.com


//*****************************************************************************
//  Tuning of the template's behaviour.
//
//  Switching of the i/o binding between files (input.txt and output.txt in the
//  program starting folder) and standart streams. Just comment/uncomment
//  necessary assigments of the <input_binding> and <output_binding> params.

enum IOBinding { File, StdStream };

static const IOBinding InputBinding = File;
//static const IOBinding InputBinding = StdStream;

static const IOBinding OutputBinding = File;
//static const IOBinding OutputBinding = StdStream;

//  Basic handling of the input and output by main function.

enum IOHandlingFlag {
  MultipleTestCases = 0x1,
  PrintCaseNumberInCodeJamStyle = 0x2
};

static const int IOHandlingFlags =
    MultipleTestCases|PrintCaseNumberInCodeJamStyle;


//*****************************************************************************
//  Set of the most common includes, declarations and definitions necessary all
//  around. Keep this section in sync with "global.h".

#include <cmath>
#include <cassert>
#include <climits>
#include <cstdint>
#include <cstring>

#include <fstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

typedef std::vector <int> IVec;
typedef std::unordered_set <int> ISet;


//*****************************************************************************
//  Implementation of the problem solution.

std::istream *input = &std::cin;
std::ostream *output = &std::cout;

class Problem {
public:
  Problem();
  ~Problem();
  void solve();

private:
  uint64_t Reinterpret(uint64_t x, int base);

};

Problem::Problem()
{

}

Problem::~Problem() {

}

void Problem::solve() {
  int N, J;
  *input >> N >> J;
  *output << '\n';

  uint64_t divisors[9], x = 1 + pow(2, N-1);
  for (int j = 0; j < J; ++j) {
    bool ready = false;
    do {
      ready = true;
      for (int i = 0; i < 9; ++i) {
        uint64_t number = Reinterpret(x, i+2);
        int k = 2, max = number < 100 ? number : 100;
        while ((k < max) && (number%k)) ++k;
        if (k == max) { ready = false; break; }
        else divisors[i] = k;
      }
      x += 2;
    } while(!ready);
    *output << Reinterpret(x-2, 10) << ' ';
    for (int i = 0; i < 9; ++i)
      *output << divisors[i] << ' ';
    *output << '\n';
  }
}

uint64_t Problem::Reinterpret(uint64_t x, int base) {
  uint64_t res = 0, add = 1;
  while (x) {
    if (x&1) res += add;
    add *= base; x >>= 1;
  }
  return res;
}

//*****************************************************************************
//  Setup of <input> and <output> binding to input.txt and output.txt files if
//  necessary.

void InitIOStreams() {
  std::ios_base::sync_with_stdio(false);
  if (InputBinding == File) input = new std::ifstream("input.txt");
  if (OutputBinding == File) output = new std::ofstream("output.txt");
}

void DeinitIOStreams() {
  if (InputBinding == File) delete input;
  if (OutputBinding == File) delete output;
}


//*****************************************************************************
//  Start-up of the solution.

int main(int argc, char *argv[]) {
  (void) argc;
  (void) argv;
  InitIOStreams();
  int num_test_cases = 1;
  if (IOHandlingFlags & MultipleTestCases) *input >> num_test_cases;
  for(int t = 1; t <= num_test_cases; ++t) {
    if (IOHandlingFlags & PrintCaseNumberInCodeJamStyle)
      *output << "Case #" << t << ": ";
    Problem p; p.solve();
  }
  DeinitIOStreams();
  return 0;
}
