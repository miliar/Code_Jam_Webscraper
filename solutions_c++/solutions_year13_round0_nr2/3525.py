#include <stdio.h>

int T;
int N, M;
int a[100][100];
int b[100][100];
int i, j, n;
int h[101];
int t[100];
int len;

bool canRow(int r, int v)
{
  int i;
  for (i = 0; i < M; i++)
    if (a[r][i] > v) return false;
    
  return true;  
}

bool canCol(int c, int v)
{
  int i;
  for (i = 0; i < N; i++)
    if (a[i][c] > v) return false;
    
  return true;  
}


void fillRow(int r, int v)
{
  int i;
  for (i = 0; i < M; i++) {
    if (a[r][i] == v) a[r][i] = 0;
    if (b[r][i] == 0) b[r][i] = v;
  }
  
  return;
}

void fillCol(int c, int v)
{
  int i;
  for (i = 0; i < N; i++) {
    if (a[i][c] == v) a[i][c] = 0;
    if (b[i][c] == 0) b[i][c] = v;
  }
  
  return;
}

void printa()
{
  int i, j;
  for (i = 0; i < N; i++) {
    for (j = 0; j < M; j++)
      printf("%d ", a[i][j]);
    printf("\n");
  }
  return;
}

void printb()
{
  int i, j;
  for (i = 0; i < N; i++) {
    for (j = 0; j < M; j++)
      printf("%d ", b[i][j]);
    printf("\n");
  }
  return;
}

bool check()
{
  int i, j, n;
  
  for (n = 0; n < len; n++) {
    int v = t[n];
   // printf("v=%d\n", v);
    for (i = 0; i < N; i++) {
      for (j = 0; j < M; j++) {      
	if (a[i][j] == v) {
	    bool cr = canRow(i, v);
	    bool cc = canCol(j, v);
	    if (!cr && !cc) return false;
	    
	    if (cr) fillRow(i, v);
	    if (cc) fillCol(j, v);
	}
      }
    }
    //printa();
   //printb();
  }
 
  return true;  
}

int main() {

  scanf("%d", &T);
  
  int cs = 0;
  while (T--) {
    cs++;
    
    scanf("%d %d", &N, &M);
    
    for (i = 0; i <= 100; i++) h[i] = 0;
    
    for (i = 0; i < N; i++)
      for (j = 0; j < M; j++) {
	scanf("%d", &a[i][j]);
	h[a[i][j]] = 1;
	b[i][j] = 0;
      }
    
    len = 0;
    for (i = 0; i <= 100; i++)
      if (h[i] == 1) {
	t[len] = i; len++;
      }
    
    if (check())      
      printf("Case #%d: YES\n", cs);  
    else
      printf("Case #%d: NO\n", cs);  
  }
  
  return 0;
}