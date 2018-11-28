#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<deque>

using namespace std;

const int MAX_SIZE = 1000000;
const char* OUTPUT = "Case #%d: ";

typedef deque<char> buffer;
typedef buffer::iterator pointer;

static inline int parseInteger() {
  static int result = 0;
  scanf("%d", &result);
  return result;
}

static inline char* initBuffer() {
  return (char*)malloc(MAX_SIZE*sizeof(char));
}

static inline void showNewline() {
  printf("\n");
}

static inline void showHeader(int testCaseId) {
  printf(OUTPUT, testCaseId);
}

static inline void showChar(char element) {
  printf("%c", element);
}

static inline void parseString(char* buffer) {
  scanf("%s\n", buffer);
}

static inline void flush(pointer begin, pointer end) {  
  while(begin != end) {
    showChar(*begin);
    ++begin;
  }
}

static inline void process(char* input) {
  static buffer buff;  
  buff.push_back(input[0]);
  for(unsigned int i=1; i<strlen(input); ++i) {
    char first = *(buff.begin());
    if(input[i] < first) {
      buff.push_back(input[i]);
    }
    else {
      buff.push_front(input[i]);
    }
  } 
  flush(buff.begin(), buff.end());
  buff.clear();
}

static inline void execute() {
  static char* input = initBuffer();  
  parseString(input);  
  process(input);  
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
