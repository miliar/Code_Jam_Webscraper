#include <stdio.h>
#include <cstdio>

void setFlags(int N, int &flags);
bool checkFlags(int flags);

int main(int argc, char** argv) 
{
  if (argc < 2) {
    printf("Usage: main <input_file>\n");
    return 1;
  }
  FILE* fp;
  fp = fopen(argv[1], "r");
  int T = 0;
  int flags = 0x0;
  fscanf(fp, "%d", &T);
  for (int i=0; i < T; i++) {
    int N = 0;
    int inc = 1;
    fscanf(fp, "%d", &N);
      while (true) {	  
      if (N == 0) {
	printf("Case #%d: INSOMNIA\n", i+1);
	break;
      }
      setFlags(inc * N, flags);
      if (checkFlags(flags)) {
	flags = 0x0;
	printf("Case #%d: %d\n", i+1, inc * N);
	break;
      }
      inc++;
    }
  }
  return 0;
}

void setFlags(int N, int &flags) {
  while (N > 0){
    int val = N % 10;
    flags |= (0x1 << val);
    N /= 10;
  }
}

bool checkFlags(int flags) {
    return ((flags & 0x3FF) == 0x3FF);
}

