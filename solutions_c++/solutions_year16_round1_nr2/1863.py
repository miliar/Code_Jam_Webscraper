#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;

const int MAX_SIZE = 5000;
const char* OUTPUT = "Case #%d:";

typedef set<int> buffer;
typedef buffer::iterator pointer;

static inline int parseInteger() {
  static int result = 0;
  scanf("%d", &result);
  return result;
}

static inline void showNewline() {
  printf("\n");
}

static inline void showHeader(int testCaseId) {
  printf(OUTPUT, testCaseId);
}

static inline void showInteger(int element) {
  printf(" %d", element);
}

static inline void clear(int* input, buffer* buff) {
  buff->clear();
  for(int i=0; i<MAX_SIZE; ++i) {
    input[i] = 0;
  }
}

static inline void flush(pointer begin, pointer end) {
  while(begin != end) {
    showInteger(*begin);
    ++begin;
  }
}

static inline int getSize() {
  int number = parseInteger();
  return number*(2*number-1);
}

static inline void parse(int* input) {
  int size = getSize();
  for(int i=0; i<size; ++i) {
    ++input[parseInteger()]; 
  }
}

static inline void process(int* input, buffer* buff) {
  parse(input);
  for(int i=0; i<MAX_SIZE; ++i) {
    if(input[i]%2 == 1) {
      buff->insert(i);
    }
  }
}

static inline void execute() {
  static int input[MAX_SIZE];
  static buffer buff;
  clear(input, &buff);
  process(input, &buff);
  flush(buff.begin(), buff.end());
}

static inline int run(int tests) {
  for(int i=1; i<=tests; ++i) {
    showHeader(i);
    execute();
    showNewline();
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);
}
