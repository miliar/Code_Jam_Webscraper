#include <cstdio>
#include <cstring>

int N; // vertical   width
int M; // horizontal width
int a[10][10]; // height of each square
int b[10][10]; // tmp

void readBoard()
{
  scanf("%d %d", &N, &M);
  for ( int i=0; i<N; ++i )
    for ( int j=0; j<M; ++j )
      scanf("%d", &a[i][j]);
}

void cutRow(const int i)
{
  for ( int j=0; j<M; ++j )
    b[i][j] = 1;
}

void cutCol(const int j)
{
  for ( int i=0; i<N; ++i )
    b[i][j] = 1;
}

bool boardEqual()
{
  for ( int i=0; i<N; ++i )
    for ( int j=0; j<M; ++j )
      if ( a[i][j] != b[i][j] )
	return false;
  return true;
}

void printBoard()
{
  for ( int i=0; i<N; ++i, putchar('\n') )
    for ( int j=0; j<M; ++j )
      printf("%d ", b[i][j]);
}

bool possible()
{
  int bi, bj;
  int bi_max = 1 << N;
  int bj_max = 1 << M;
  for ( int bi=0; bi<bi_max; ++bi ) {
    for ( int bj=0; bj<bj_max; ++bj ) {
      for ( int i=0; i<N; ++i )
	for ( int j=0; j<M; ++j )
	  b[i][j] = 2;
      for ( int i=0; i<N; ++i )	if ( (bi>>i)&1 ) cutRow(i);
      for ( int j=0; j<M; ++j )	if ( (bj>>j)&1 ) cutCol(j);
      if ( boardEqual() ) {
	//printf("bi=%d, bj=%d\n", bi, bj);
	//printBoard();
	return true;
      }
    }
  }
  return false;
}

int main()
{
  int T; // number of test cases
  scanf("%d", &T);
  for ( int i=1; i<=T; ++i ) {
    readBoard();
    printf("Case #%d: %s\n", i, possible()?"YES":"NO");
  }
}
