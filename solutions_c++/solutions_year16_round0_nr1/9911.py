#include <cstdio>
#include <cstdlib>
#include <cstring>

void updateSeen(bool *S, int n);
bool allSeen(bool *S);

int main(int argc, char *argv[]) {

  int T, N;

  scanf("%d", &T);
  
  for(int t=1; t<=T; t++) {

    scanf("%d", &N);
    
    if( N>0 ) {
      bool seen[10];
      memset(seen, false, 10*sizeof(bool));
      
      int n = N;
      while( !allSeen(seen) ) {
	updateSeen( seen, n);
	n += N;
      }
      
      printf("Case #%d: %d\n", t, n-N);
    }
    else
      printf("Case #%d: INSOMNIA\n", t);
  }

  return 0;
}


void updateSeen(bool *S, int n) {
  while( n>0 ) {
    S[ n%10 ] = true;
    n /= 10;
  }
}

bool allSeen(bool *S) {
  for(int i=0; i<10; i++) {
    if( !S[i] )
      return false;
  }

  return true;
}
