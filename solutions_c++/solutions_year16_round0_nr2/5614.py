#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <deque>

#define SSTR( x ) static_cast< ostringstream & >( \
        ( ostringstream() << dec << x ) ).str()

using namespace std;

int readInt() {
  string line;
  int result;
  getline(cin, line);
  stringstream(line) >> result;

  return result;
}

void printCaseResult(int caseNo, string result) {
  cout << "Case #" << caseNo << ": " << result << endl;
}

deque<bool> prepareDeque() {
  string line;
  getline(cin, line);
  //cout << line << " ";
  deque<bool> dq = deque<bool>();
  for (string::const_iterator it = line.begin(); it != line.end(); it++) {
    dq.push_back(*it == '+');
  }

  return dq;
}

int work(deque<bool> &dq) {
  int flips = 0;
  bool prev = dq.front();
  for (deque<bool>::const_iterator crit = dq.begin(), 
                                   crend = dq.end(); 
       crit != crend; 
       crit++) {
    bool curr = *crit;
    if (curr != prev) {
      flips++;
      prev = curr;
    }
  }

  if (!prev) {
    flips++;
  }

  return flips;
}

void solveCase(int caseNo) {
  deque<bool> dq = prepareDeque();
  int flips = work(dq);
  printCaseResult(caseNo, SSTR(flips));
}


int main() {
  const int totalCases = readInt();
  int casesLeft = totalCases;
  while (casesLeft-- > 0) {
    solveCase(totalCases - casesLeft);
  }

  return 0;
}
