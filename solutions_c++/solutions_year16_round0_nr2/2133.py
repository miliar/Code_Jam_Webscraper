#include <iostream>
#include <fstream>
#include <unordered_map>
#include <queue>
#include <bitset>

constexpr unsigned STACK_SIZE = 100;
using PancakeStack = std::bitset<STACK_SIZE>;
using PancakeMemos = std::unordered_map<PancakeStack, int>;
using PrevStateLog = std::unordered_map<PancakeStack, PancakeStack>;

struct Subproblem {
  std::string s;
  int steps = 0;
};

using SubproblemManager = std::queue<PancakeStack>;

int lastUnhappy(PancakeStack s) {
  for (int i = STACK_SIZE - 1; i >= 0; --i) {
    if (!s[i]) return i;
  }
  return -1;
}

int posSeq(PancakeStack s) {
  int i = 0;
  while (s[i]) ++i;
  return i;
}

void flipToPos(PancakeStack& s, int pos) {
  for (int i = 0, j = pos; i <= j; ++i, --j) {
    bool tmp = s[i];
    s[i] = !s[j];
    s[j] = !tmp;
  }
}

int solve(PancakeStack s) {
  int nFlips = 0;
  for(int pos; (pos = lastUnhappy(s)) >= 0; ++nFlips) {
    int pSeqAtFront = posSeq(s);
    if (pSeqAtFront) {
       flipToPos(s, pSeqAtFront - 1);
       ++nFlips;
    }
    flipToPos(s, pos);
  }
  return nFlips;
}

PancakeStack readProblem(std::istream& in) {
  PancakeStack p;
  p.flip();

  char c;

  for(int pos = 0; in.get(c) && c != '\n'; ++pos) {
    p.set(pos, c == '+');
  }

  return p;
}

int main(int argc, char* argv[]) {

  if (argc < 3) {
    std::cout << "usage: " << argv[0] << " <infile> <outfile>" << std::endl;
    return 0;
  }

  std::ifstream infile {argv[1]};
  std::ofstream outfile {argv[2]};

  int nCases;
  infile >> nCases;
  infile.ignore(100, '\n');

  PancakeMemos memos;

  for (int caseNum = 1; caseNum <= nCases; ++caseNum) {
    auto s = readProblem(infile);

    outfile << "Case #" << caseNum << ": ";
    outfile << solve(s);
    outfile << std::endl;
  }
}

