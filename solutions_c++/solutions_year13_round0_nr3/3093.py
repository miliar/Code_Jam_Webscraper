//------------------------------------------------------------------------------
// Copyright (c) 2013 Mineyuki Iwasaki. All rights reserved.
//------------------------------------------------------------------------------
#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <cmath>
#include <algorithm>
//#define LOG(f,...) fprintf(stderr, f, __VA_ARGS__)
#define LOG(f,...)
using namespace std;

int GetDigit(char* word) {
  int digit = 0;
  while (*word) {
    ++word;
    ++digit;
  }
  return digit;
}

void Increment(char* word) {
  int digit = GetDigit(word);
  int index = digit / 2;
  if (digit % 2 == 0) {
    --index;
  }
  while (word[index] == '9') {
    word[index] = '0';
    --index;
  }
  if (index >= 0) {
    ++word[index];
  } else {
    for (int i=0; i!=digit; ++i) {
      word[digit - i] = word[digit - i - 1];
    }
    word[digit+1] = NULL;
    word[0] = '1';
  }
}

void Mirror(char* word) {
  int digit = GetDigit(word);
  for (int i = 0; i != digit / 2; ++i) {
    word[digit - i -1] = word[i];
  }
}

bool Compare(char* small, char* large) {
  LOG("Compare %s, %s\n", small, large);
  if (GetDigit(small) < GetDigit(large)) {
    LOG("A\n");
    return true;
  } else if (GetDigit(small) > GetDigit(large)) {
    LOG("B\n");
    return false;
  } else {
    while (*small) {
      if (*small < *large) {
        LOG("C %c, %c\n", *small , *large);
        return true;
      } else if (*small > *large) {
        LOG("D %c, %c\n", *small , *large);
        return false;
      }
      ++small;
      ++large;
    }
  }
  LOG("E\n");
  return true;
}

bool IsPlindromes(uint64_t value) {
  char word[102];
  sprintf(word, "%d", value);
  LOG("Plind; %s\n", word);
  int digit = GetDigit(word);
  for (int i=0; i!=digit/2; ++i) {
    if (word[i] != word[digit - i - 1]) {
      return false;
    }
  }
  return true;
}

bool CheckSqrt(char *word) {
  uint64_t value = atoi(word);
  uint64_t a = (uint64_t)sqrt((double)value);
  uint64_t b = a + 1;
  LOG("a=%d, b=%d, aa=%d, bb=%d value=%d\n",
      a, b, a*a, b*b, value);
  if (a * a == value) {
    return IsPlindromes(a);
  }
  if (b * b == value) {
    return IsPlindromes(b);
  }
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  char A[102];
  char B[102];
  // Loop
  for (int t = 0; t != T; ++t) {
    int result = 0;
    // Input size.
    scanf("%s ", A);
    scanf("%s", B);
    LOG("----------------------------------------------------\n");
    LOG("%s/%s, %d,%d----------------------------------------------------\n", A, B, GetDigit(A), GetDigit(B));
    LOG("----------------------------------------------------\n");

    char C[102];
    for (int i = 0; i != 102; ++i) {
      C[i] = A[i];
    }
    Mirror(C);

    if (!Compare(A, C)) {
      Increment(C);
    }

    while (1) {
      LOG("Check %s\n", C);
      if (CheckSqrt(C)) {
        LOG("Add\n");
        ++result;
      }

      // Make numbers.
      LOG("A:%s,", C);
      Increment(C);
      LOG("B:%s", C);
      Mirror(C);
      LOG("C:%s\n", C);

      // End
      if (!Compare(C, B)) {
        LOG("Break %s, %s\n", C, B);
        break;
      }
    }

    // Result.
    printf("Case #%d: %d\n", t+1, result);
  }
  return 0;
}
