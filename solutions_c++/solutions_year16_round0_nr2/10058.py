#include <cstdio>
#include <cstdlib>
#include <cstring>

int min(int a, int b) {
  return a < b ? a : b;
}
int happyflips(char *S, int N, int p);
void flip(char *S, int p);

int main(int argc, char *argv[]) {

  int T, N;

  scanf("%d", &T);

  char pancakes[101];
  for(int t=1; t<=T; t++) {
    scanf("%s", pancakes);

    int nPK = strlen( pancakes );

    printf("Case #%d: %d\n", t, happyflips(pancakes, nPK, 0) );
  }

  return 0;
}

int happyflips(char *S, int N, int p) {
  if( p==N ) {
    bool happy = true;
    for(int i=0; i<N && happy; i++) {
      if( S[i] != '+' )
	happy = false;
    }
    
    if( happy )
      return 0;
    return N+1;
  }

  //No flip
  int noFlip = happyflips(S, N, p+1);

  //Do flip
  flip(S, p);
  int doFlip = 1 + happyflips(S, N, p+1);
  flip(S, p);

  return min(noFlip, doFlip);
}

void flip(char *S, int p) {
  int i, j;
  for(i=0, j=p; i<j; i++, j--) {
    char aux = S[i];
    S[i] = S[j] == '+' ? '-' : '+';
    S[j] =  aux == '+' ? '-' : '+';
  }

  if( i==j )
    S[i] = S[i] == '+' ? '-' : '+';
}
