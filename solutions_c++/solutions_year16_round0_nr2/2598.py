#include<stdio.h>
#include<stdlib.h>

using namespace std;

const char* OUTPUT = "Case #%d: %d\n";
const char PLUS_CHAR = '+';
const char MINUS_CHAR = '-';
const int PLUS = 1;
const int MINUS = 0;
const char LF = '\n';

typedef struct {
  int length;
  int first;
  int last;
} stack;

static inline int parseInteger() {
  static int res = 0;
  scanf("%d", &res);
  return res;
}

static inline int parseCharacter() {
  static char res;
  scanf("%c", &res);
  return res;
}

static inline void parseNewline() {
  scanf("\n");
}

static inline void showResult(int testCaseId, int result) {
  printf(OUTPUT, testCaseId, result);
}

static inline void clearStack(stack* input) {
  input->length = 0;
  input->first = 0;
  input->last = 0;
}

static inline void init(stack* input, int token) {
  input->length = 1;
  input->first = token;
}

static inline void update(stack* input, int token) {
  if(input->last != token) {
    ++input->length;
  }
}

static inline void changeState(stack* input, int token) {
  if(input->length == 0) {
    init(input, token);    
  }
  else {
    update(input, token);
  }
  input->last = token;
}

static inline bool parseNext(stack* input) {
  char nextChar = parseCharacter();
  bool result = true;
  switch(nextChar) {
  case PLUS_CHAR:
    changeState(input, PLUS);
    break;
  case MINUS_CHAR:
    changeState(input, MINUS);
    break;
  case LF:
    result = false;
    break;
  default:
    break;
  }
  return result;
}

static inline void parseStack(stack* input) {
  bool next = true;
  clearStack(input);
  while(next) {
    next = parseNext(input);
  }
}

static inline int findStackType(stack* input) {  
  return (input->first+input->length)%2;
}

static inline void execute(int testCaseId) {
  static stack pancakes = {0,0,0};
  static int result = 0;
  parseStack(&pancakes);
  result = pancakes.length-1+findStackType(&pancakes);
  showResult(testCaseId, result);
}

static inline int run(int tests) {
  parseNewline();
  for(int i=1; i<=tests; ++i) {
    execute(i);
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);
}
