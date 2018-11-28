#include <stdio.h>
#include <string.h>
#define max(a,b) (a>b?a:b)

int matrix[1000][1000];
int colHeigh[1000];
int rowHeigh[1000];

int main() {
  int nTests;
  scanf("%i", &nTests);
  for (int test=1; test<=nTests; test++) {
    int N, M;
    scanf("%i%i", &N, &M);
    memset(colHeigh, 0, sizeof(colHeigh));
    memset(rowHeigh, 0, sizeof(rowHeigh));
    
    for (int row=0; row<N; row++) {
      for (int col=0; col<M; col++) {
	scanf("%i", &matrix[row][col]);
	colHeigh[col] = max(colHeigh[col], matrix[row][col]);
	rowHeigh[row] = max(rowHeigh[row], matrix[row][col]);
      }
    }
    
    bool possible = true;
    for (int row=0; row<N; row++) {
      for (int col=0; col<M; col++) {
	possible = possible && 
	    ((matrix[row][col] == colHeigh[col]) || (matrix[row][col] == rowHeigh[row]));
      }
    }

    printf("Case #%i: %s\n", test, possible?"YES":"NO");
  }

  return 0;
}