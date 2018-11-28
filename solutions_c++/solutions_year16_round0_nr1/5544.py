#include <iostream>
#include <string>
#include <sstream>

#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;

const int GOAL_SUM = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10;

int readInt() {
  string line;
  int result;
  getline(cin, line);
  stringstream(line) >> result;

  return result;
}

void clearArray(bool (&arr) [10]) {
  for(int i = 0; i < 10; i++) {
    arr[i] = false;
  }
}

void printCaseResult(int caseNo, string result) {
  cout << "Case #" << caseNo << ": " << result << endl;
}

int readDigits(int startNumber, bool (&result) [10]) {
  int currentNumber = startNumber;
  int sum = 0;

  do {
    int digit = currentNumber % 10;
    if (!result[digit]) {
      result[digit] = true;
      if (digit == 0) {
        sum += 10;
      } else {
        sum += digit;
      }

      if (sum == GOAL_SUM) {
        return sum;
      }
    }

    currentNumber /= 10;
  } while (currentNumber != 0);

  return sum;
}

void solveCase(int caseNo, bool (&arr) [10]) {
  const int start = readInt();
  int current = start;
  int mult = 1;
  int sum = 0;

  if (start == 0) {
    printCaseResult(caseNo, "INSOMNIA");
    return;
  }

  while (sum != GOAL_SUM) {
    sum += readDigits(current, arr);

    if(sum == GOAL_SUM) {
      printCaseResult(caseNo, SSTR(current));
      return;
    }

    mult += 1;
    current = mult * start;
  }
}

int main() {
    string sCases;
    int totalCases = readInt();
    int casesLeft = totalCases;
    bool arr [10] = { false, false, false, false, false, false, false, false, false, false };

    while(casesLeft-- > 0) {
      clearArray(arr);

      solveCase(totalCases - casesLeft, arr);
    }


    return 0;
}
