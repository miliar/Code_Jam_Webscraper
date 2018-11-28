#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for ( int t=1; t<=T; ++t ) {
    int N, X, S[10000];
    scanf("%d %d", &N, &X);
    for ( int i=0; i<N; ++i ) scanf("%d", &S[i]);
    sort(S, S+N);
    int L = 0;
    int R = N-1;
    int cd_count = 0;
    while ( L <= R ) {
      if ( L==R ) {
	++cd_count;
	break;
      }
      else if ( S[L] + S[R] <= X ) {
	++L;
	--R;
	++cd_count;
      }
      else {
	--R;
	++cd_count;
      }
    }
    printf("Case #%d: %d\n", t, cd_count);
  }
}
