#include "codejamhelper.h"

int main(int argc, char** argv) {
  Test(R"(
6
4 11111
1 09
5 110011
0 1
5 009999
5 900111
)",
       R"(
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 2
Case #6: 0
)");

  InitCodeJam();

  ForEachTestCase() {
    auto vals = ReadVec<string>();
    auto chardigits = vals[1];
    vector<int> digits;
    for (char c : chardigits) {
      digits.push_back(c - '0');
    }
    int nb_invites = 0;
    int applause = 0;
    int shy_level = 0;
    for (int n : digits) {
      if (applause < shy_level) {
        int missing = shy_level - applause;
        nb_invites += missing;
        applause += missing;
      }
      applause += n;
      shy_level++;
    }
    Print(nb_invites);
  }
  return EXIT_SUCCESS;
}
