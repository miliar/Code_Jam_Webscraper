#include <stdio.h>
#include <vector>

using namespace std;

int T, R, C, M;
int f[50][50];
int a[50][50];
int i, j, k;
vector <char> mask, sol;
int di[8] = {-1, -1, -1,  0, 0,  1, 1, 1};
int dj[8] = {-1,  0,  1, -1, 1, -1, 0, 1};
int soli, solj;

void print(vector <char> v)
{
  int i;
  for (i = 0; i < v.size(); i++)
    printf("%d ", (int)v[i]);
  printf("\n");
  return;
}

void copy()
{
  int i, j;
  for (i = 0; i < R; i++)
    for (j = 0; j < C; j++)
      a[i][j] = f[i][j];
}

int count()
{
  int i, j;
  int c = 0;
  for (i = 0; i < R; i++)
    for (j = 0; j < C; j++)
      if (a[i][j] == -1) c++;
      
  return c;    
}

void printa()
{
  int i, j;  
  for (i = 0; i < R; i++) {
    for (j = 0; j < C; j++) 
      printf("%d", a[i][j]);
    printf("\n");
  }
      
  return;    
}


void fill(int i, int j)
{
  a[i][j] = 0;
  int k;  
  for (k = 0; k < 8; k++) {
    int in = i + di[k];
    int jn = j + dj[k];
    if (0 <= in && in < R && 0 <= jn && jn < C) {
      if (a[in][jn] == 9) {a[i][j]++; continue;}      
    }
  }  
  
  if (a[i][j] == 0) {
    for (k = 0; k < 8; k++) {
      int in = i + di[k];
      int jn = j + dj[k];
      if (0 <= in && in < R && 0 <= jn && jn < C) {
        if (a[in][jn] == -1) fill(in, jn);
      }
    }      
  }
  
  return;
}

bool check(vector <char> v)
{
  int i, j, k;  
  i = 0; j = 0;
  for (k = 0; k < v.size(); k++) {
    if (v[k] == 1)
      f[i][j] = 9;
    else
      f[i][j] = -1;
    j++;
    if (j == C) {i++; j = 0;}
  }
  
  for (i = 0; i < R; i++) {
    for (j = 0; j < C; j++) {
      if (f[i][j] == 9) continue;
      copy();
      fill(i, j);
      int cnt = count();
      if (cnt == 0) {
	soli = i; solj = j;      
	return true;
      }
    }
  }

  
  return false;
}

bool build(int pos, vector <char> v)
{
  //print(v);
  if (check(v)) {
    sol = v;
    return true;
  }
  
  if (pos < 0) return false;
  
  int i;
  for (i = pos; i < v.size()-1; i++) {
    if (v[i+1] == 1) break;
    v[i] = 0; v[i+1] = 1;
    if (build(pos-1, v)) return true;
  }
  return false;
}

int main() {

  scanf("%d", &T);
  int c = 0;
  while (T--) {
    c++;
    printf("Case #%d:\n", c);
    
    scanf("%d %d %d", &R, &C, &M);
    
    mask.clear();
    mask.resize(R*C);
    for (i = 0; i < M; i++) mask[i] = 1;
    
    bool res = build(M-1, mask);
    
    if (res == false) {
      printf("Impossible\n");
      continue;
    }
    
    //print(sol);
    //printa();
    
    for (i = 0; i < R; i++) {
      for (j = 0; j < C; j++) {
	if (i == soli && j == solj) {
	  printf("c"); continue; 
	}      
	if (f[i][j] == 9)
	  printf("*");
	else
	  printf(".");
      }
      printf("\n");
    }
    
    
  }
  
  return 0;
}