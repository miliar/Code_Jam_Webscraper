#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int N, M, R;
int A[20][20];

const int INF = 1 << 30;

int backtrack( int r, int c, int rem ) {
   
   if( c == M ) {
	r = r + 1;
	c = 0;
   }

   if( r == N ) {
	return (rem == 0) ? 0 : INF; 
   }
    
   if( rem == 0 ) return 0;

   int take = 0;

   if( r > 0 && A[r-1][c] )
       take++;
   if( c > 0 && A[r][c-1] )
       take++;
    
    int ret = INF;

    A[r][c] = 1;
    ret = backtrack(r, c+1, rem-1) + take;
    A[r][c] = 0;

    ret = min(ret, backtrack(r, c+1, rem));
}

int main( void ) {
    int T;
    scanf("%i", &T);

    for( int t = 1; t <= T; t++ ) {
	scanf("%i %i %i", &N, &M, &R);
	memset(A, 0, sizeof(A));
	printf("Case #%i: %i\n", t, backtrack(0, 0, R));
    }

    return 0;
}
