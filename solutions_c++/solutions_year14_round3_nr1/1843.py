#include <stdio.h>
#include <assert.h> 
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <list>

#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define false 0
#define true 1
#define bool int
#define read fscanf

bool isInFile, isOutFile;
FILE *inFile, *outFile;

void write(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    vprintf(fmt, ap);
    if (isOutFile)
        vfprintf(outFile, fmt, ap);
    va_end(ap);
}

void solveOne();

int main(int argc, char **argv) {
  int T, i;

  isInFile = (argc > 1);
  if (isInFile) {
    inFile = fopen(argv[1], "r");
    if (inFile == NULL) {
      printf("infile not found");
      exit(0);
    }
  } else {
    inFile = stdin;
  }
  isOutFile = (argc > 2);
  if (isOutFile) {
    outFile = fopen(argv[2], "w");
    if (outFile == NULL) {
      printf("outfile error");
      exit(0);
    }
  }

  read(inFile, "%d\n", &T);
  for (i = 1; i <= T; i++) {
    write("Case #%d: ", i);
    solveOne();
    write("\n");
  }
  return 0;
}

void solveOne()
{
  int P, Q;
  read(inFile, "%d/%d\n", &P, &Q);
  int p = P;
  int q = Q;
  if ( 0 == (q % p)) {
    p = 1;
    q = q / p;
  }

  int a = 0;
  int e = 0;
  while(1 != q ) 
  {
    int m = q % 2;
    q = q / 2;
    if(0 != m) {
      break;
    }
    ++e;

    if(0 == p) continue;

    m = p % 2;
    p = p / 2;
    if(( 0 == p ) && (a == 0)) {
      a = e;
    }
  }
  if(0 == a) {
    write("impossible");
  } else {
    write("%d", e - a + 1);
  }
}
