#include <cstdlib>
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

char line[105];


int foo() {
  int len = strlen(line);
  int flips = 0, i = len - 1;
  bool flag = false;
  
  while (i >= 0 && (line[i] == '+')) 
    --i;

  if (i >= 0) 
    ++flips;

  bool neg = true;
  for (; i >= 0; --i) {
    if (line[i] == '-' && !neg) {
      ++flips;
      neg = true;
    }
    else if (line[i] == '+' && neg) {
      ++flips;
      neg = false;
    }
  }

  return flips;
}

int main() {
  int t;
  FILE *fin = NULL, *fout = NULL;

  fin = fopen("inputB.txt", "r");
  fout = fopen("outputB.txt", "w");

  fscanf(fin, "%d", &t);
  for (int i = 1; i <= t; ++i) {
    fscanf(fin, "%s", line);
    fprintf(fout, "Case #%d: %d\n", i, foo());
  } 



  fclose(fin);
  fclose(fout);
	return 0;
}