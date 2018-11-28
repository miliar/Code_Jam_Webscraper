#include<iostream>
#include<cstdio>

int N,M;
int a[200][200];

int findmin(int& minr, int& minc) {
  int min = 10000;
  for (int i = 0; i < N; i++) 
    for (int j = 0; j < M; j++)
      if(a[i][j] >=0 && a[i][j] <min) {
	min = a[i][j];
	minr = i;
	minc = j;
      }
  return min;
}

bool testrow(int row, int height) {	
  for (int j = 0; j < M; j++) {	
    if(a[row][j] > height)
      return false;
  }
  return true;
}	


bool testcolumn(int column, int height) {	
  for (int i = 0; i < N; i++) {	
    if(a[i][column] > height)
      return false;
  }
  return true;
}


void markrow(int row) {
  for(int j = 0; j < M; j++) {
    a[row][j] = -1;
  }
}

void markcolumn (int column) {	
  for (int i = 0; i < N; i++) {
    a[i][column] = -1;
  }
}


void work(int ca)
{
  scanf("%d%d",&N,&M);
  for(int i = 0; i < N; i++)
    for(int j = 0; j < M; j++) {
      scanf("%d", &a[i][j]);
    }
  while(true) {
    int minr, minc;
    int min = findmin(minr, minc);
    if (min > 100)
      break;
    if (testrow(minr, min)) {
      markrow(minr);
      continue;
    }
    else if (testcolumn(minc, min)) {
      markcolumn(minc);
      continue;
    }
    else {
      printf("Case #%d: NO", ca);
      return;
    }
  }
  printf("Case #%d: YES", ca);
}

bool test(int r, int c) {
  bool row = true, column = true; 
  for(int i = 0; i < N; i++)
    if(a[i][c] > a[r][c])
      column = false;
  for (int j = 0; j < M; j++)
    if(a[r][j] > a[r][c])
      row = false;
  return row || column;
}

void work2(int ca) 
{
  scanf("%d%d",&N,&M);
  for(int i = 0; i < N; i++)
    for(int j = 0; j < M; j++) {
      scanf("%d", &a[i][j]);
    }
  for(int i = 0; i < N; i ++) 
    for (int j = 0; j < M; j++) 
      if(!test(i,j)) {
	printf("Case #%d: NO", ca);
	return;
      }
  printf("Case #%d: YES", ca);
}
int main()
{
  int T;
  scanf("%d",&T);
  int b = T;
  while(T-- > 0) {
    work2(b-T);
    printf("\n");
  }
}
