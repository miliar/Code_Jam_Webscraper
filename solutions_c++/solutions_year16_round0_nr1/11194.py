#include <cstdio>
#include <cstring>
#include <malloc.h>
#include <fcntl.h>


#define	SMALL_SAMPLE_SET	0

#if SMALL_SAMPLE_SET
#define	C	1
#define	D	1
#define	N	10
#else
#define	C	36
#define	D	28
#define	N	100
#endif

#define MASK  0x03ff

void setBits(short* pBitmap, int n) {
  int r;
  while (n) {
    r = n %10;
    *pBitmap |= 1 << r;
    n /= 10;
  }
}

int process(int n) {
  int result = -1;
  if (n == 0) {
    return result;
  }

  short bitmap = 0;
  setBits(&bitmap, n);
  int i = 1;
  while (bitmap != MASK) {
    setBits(&bitmap, n*++i);
  }

  return n*i;
}


int ParseInput(
	char *pcszFileName
	)
{
  int T;
  int n;
  int i,j;
  FILE *fp, *fout;
  char szOpp[2];
  char szPairs[3];
  char szInput[N];
  int iPairs,iOpposites, iInputLength; 

  if (NULL == pcszFileName)
    return -1;

  fp = fopen(pcszFileName, "r");
  if (NULL == fp)
  {
     printf("\nAccess denied file: %s", pcszFileName);
     return -1;
  }

  fscanf(fp, "%d ", &T);

  fout = fopen("sheep_out.txt", "w");
  if (NULL == fout)
  {
     printf("\nCannot create new file.");
     return -1;
  }

  int result;
  for (i = 1; i <= T; ++i)
  {
    fscanf(fp, "%d ", &n);
    result = process(n);
    if (result != -1) {
      fprintf(fout, "Case #%d: %d\n", i, result);
    } else {
      fprintf(fout, "Case #%d: INSOMNIA\n", i);
    }
  }

  fclose(fp);
  fclose(fout);
  return 0;
}

int main(
	int argc,
	char *argv[]
	)
{
  if (2 != argc)
  {
    printf("Program expects input file as argument.\n");
    return 0;
  }

  int SequenceLen;
  ParseInput(argv[1]);
}
