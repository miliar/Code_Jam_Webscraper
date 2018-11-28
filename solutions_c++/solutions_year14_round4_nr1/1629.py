#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {

  int T;
  int N, X;
  int solution;
  int file, size[701];

  scanf("%d", &T);

  for(int t=1; t<=T; t++) {

    //Read info
    scanf("%d %d", &N, &X);

    for(int i=0; i<=700; i++)
      size[i] = 0;

    int a = 701, b = -1;

    //Read and count sizes
    for(int i=0; i<N; i++) {
      scanf("%d", &file);
      size[ file ]++;

      if( file < a ) a = file;
      if( file > b ) b = file;
    }

    //Solve
    solution = N;

    //for(int i=0; i<=100; i++)
    //  if( size[i]> 0 )
    //printf(" (%d,%d)\n", i, size[i]);
    
    for(int i=a; i<=b; i++)
      if( size[i] > 0 ) {

	for(int j=b; j>=i && size[i]>0; j--)
	  if( size[j] && i+j <= X ) {
	    int save = min( size[i], size[j] );

	    if( i==j )
	      save /= 2;

	    //printf("join [%d,%d] x %d\n", i, j, save);

	    size[i] -= save;
	    size[j] -= save;

	    solution -= save;
	  }
      }

    printf("Case #%d: %d\n", t, solution);
  }

  return 0;
}
