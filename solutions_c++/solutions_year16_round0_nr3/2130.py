#include<stdio.h>
#include<stdlib.h>

using namespace std;

const int MAX_BITSIZE = 30;
const int DIVISORS_SIZE = 9;
const int DIVISORS_OFFSET = 2;
const char* HEADER = "Case #%d:";

typedef struct {
  char bits[MAX_BITSIZE];
  int length;
} bitmask;

static inline int parseInteger() {
  static int res = 0;
  scanf("%d", &res);
  return res;
}

static inline void parseNewline() {
  scanf("\n");
}

static inline int getBitsSize(int bits) {
  if(bits > MAX_BITSIZE) {
    bits = bits%MAX_BITSIZE;
  }
  return bits;
}

static inline int getMask(int mask, int bits) {
  return mask%(1 << bits);
}

static inline void setBits(int mask, bitmask* bitmask) {
  for(int i=0; i<bitmask->length; ++i) {
    bitmask->bits[i] = mask%2;
    mask /= 2;
  }
}

static inline bitmask* generateBitMask(int mask, int bits) {
  static bitmask result = {{0}, 0};
  bits = getBitsSize(bits);
  mask = getMask(mask, bits);
  result.length = bits;
  setBits(mask, &result);
  return &result;
}


static inline void showNewline() {
  printf("\n");
}

static inline void showBits(bitmask* bitmask) {
  for(int i=bitmask->length-1; i>=0; --i) {
    printf("%d", (int)bitmask->bits[i]);
  }  
}

static inline void showHeader(int testCaseId) {
  printf(HEADER, testCaseId);
  showNewline();
}

static inline void showDivisors(long long* divisors) {
  for(int i=0; i<DIVISORS_SIZE; ++i) {
    printf(" %lld", divisors[i]);
  }
  showNewline();
}

static inline void show(bitmask* bitmask, long long* divisors) {
  showBits(bitmask);
  showBits(bitmask);
  showDivisors(divisors);
}

static inline int loadBits(int input) {
  return (input+1)/2;
}

static inline long long lpow(long long base, int exp) {
  long long result = base;
  for(int i=0; i<exp-1; ++i) {
    result *= base;
  }
  return result;
}

static inline void loadDivisors(int bits, long long* divisors, int offset) {
  for(int i=0; i<DIVISORS_SIZE; ++i) {
    divisors[i] = lpow((long long)(i+offset), bits)+1;
  }
}

static inline int getBegin(int bits) {
  return (1 << (bits-1))+1;
}

static inline void process(int mask, int bits, int size) {
  static long long divisors[DIVISORS_SIZE] = {};
  loadDivisors(bits, divisors, DIVISORS_OFFSET);
  for(int i=0; i<size; ++i) {
    bitmask* bitmask = generateBitMask(mask, bits);
    show(bitmask, divisors);
    mask+=2;
  }
}

static inline void execute() {  
  int bits = loadBits(parseInteger());
  int size = parseInteger();
  int mask = getBegin(bits);
  process(mask, bits, size);
}

static inline int run(int tests) {
  parseNewline();
  for(int i=1; i<=tests; ++i) {
    showHeader(i);
    execute();
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);
}
