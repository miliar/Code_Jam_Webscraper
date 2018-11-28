#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;

const char* OUTPUT = "Case #%d: %d\n";
const char* FAIL = "Case #%d: INSOMNIA\n";
const int digitsSize = 10;

static inline int parseInteger() {
  static int res = 0;
  scanf("%d", &res);
  return res;
}

static inline void show(int testCaseId, int result) {
  if(result < 0) {
    printf(FAIL, testCaseId);
  }
  else {
    printf(OUTPUT, testCaseId, result);
  }
}

static inline void loadDigits(set<int>* digits, int number) {
  while(number > 0) {
    digits->insert(number%digitsSize);
    number /= digitsSize;
  }
}

static inline int count(int number) {
  static set<int> digits;
  int result = 0;
  while(digits.size() < digitsSize) {
    result += number;
    loadDigits(&digits, result);        
  }
  digits.clear();
  return result;
}

static inline void execute(int testCaseId) {
  int input = parseInteger();
  int result = -1;
  if(input > 0) {
    result = count(input);
  }
  show(testCaseId, result);
}

static inline int run(int tests) {
  for(int i=1; i<=tests; ++i) {
    execute(i);
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);  
}
