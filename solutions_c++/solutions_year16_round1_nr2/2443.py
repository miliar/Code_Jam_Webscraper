#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n;
int map[51][51];
int data[101][51];
bool sol[101];
bool check[101];

int get_sol(int level) {
  int backup[51][51];
  int i,j,k,p;

  if (level == 2*n-1) { // solution
    return 1;
  }
  else {
    for (i=0; i<n; i++) {
      for (j=0; j<n; j++) {
        backup[i][j] = map[i][j];
      }
    }
    for (k=0; k<n; k++) {
      if (!sol[k]) {
        for (i=0; i<n; i++) {
          if (map[k][i] == 0 || map[k][i] == data[level][i]) {
            map[k][i] = data[level][i];
          }
          else {
            break;
          }
        }
        if (i==n) {
          sol[k] = true;
          if (get_sol(level+1) == 1)
            return 1;
          sol[k] = false;
        }
        for (i=0; i<n; i++) {
          map[k][i] = backup[k][i];
        }
      }
    }
    for (k=0; k<n; k++) {
      if (!sol[k+n]) {
        for (i=0; i<n; i++) {
          if (map[i][k] == 0 || map[i][k] == data[level][i]) {
            map[i][k] = data[level][i];
          }
          else {
            break;
          }
        }
        if (i==n) {
          sol[k+n] = true;
          if (get_sol(level+1) == 1)
            return 1;
          sol[k+n] = false;
        }
        for (i=0; i<n; i++) {
          map[i][k] = backup[i][k];
        }
      }
    }

    return 0;
  }
}

int main(void)
{
  int t,i,j,k1,k2,k3,k;
  int m1_i,m2_i;
  FILE *in = fopen("input.txt","r");
  FILE *out = fopen("output.txt","w");

  fscanf(in,"%d",&t);
  for (int l=0; l<t; l++)
  {
    fscanf(in,"%d",&n);
    for (i=0; i<2*n; i++) {
      check[i] = false;
      sol[i] = false;
    }
    for (i=0; i<n; i++)
      for (j=0; j<n; j++)
        map[i][j] = 0;

    for (i=0; i<2*n-1; i++)
    {
      for (j=0; j<n; j++)
      {
        fscanf(in,"%d",&data[i][j]);
      }
    }
/*
    for (i=0; i<n-1; i++)
    {
      m1_i=0; m2_i=0;
      for (j=0; j<2*n-1; j++) {
        if (!check[j]) {
          m1_i=j;
          break;
        }
      }
      for (j=m1_i+1; j<2*n-1; j++) {
        if (!check[j]) {
          m2_i=j;
          break;
        }
      }
      for (k3=i; k3<n; k3++)
        if (data[m1_i][k3] > data[m2_i][k3])
          break;
      if (k3!=n) {
        k3 = m2_i;
        m2_i = m1_i;
        m1_i = k3;
      }

      // make n_th row / col
      for (j=0; j<2*n-1; j++) {
        if (!check[j] && j!=m2_i && j!=m1_i) {
          for (k1=i; k1<n; k1++)
            if (data[j][k1] > data[m2_i][k1])
              break;

          for (k2=i; k2<n; k2++)
            if (data[j][k2] > data[m1_i][k2])
              break;

          for (k3=i; k3<n; k3++)
            if (data[m1_i][k3] > data[m2_i][k3])
              break;

          if (k1==n && k2==n) {
            if (k3==n) {
              m2_i = m1_i;
              m1_i = j;
            }
            else {
              m1_i = j;
            }
          }
          else if (k1==n){
            m2_i = j;
          }
        }
      }
      check[m1_i] = true;
      check[m2_i] = true;
      printf("%d %d\n", m1_i, m2_i);

      map[i][i] = data[m1_i][i];
    }
    for (i=0; i<2*n-1; i++)
      if (!check[i])
        break;
    map[n-1][n-1] = data[i][n-1];

    for (i=0; i<n; i++)
      printf("%d ",map[i][i]);
    printf("\n");
*/
    if (get_sol(0) == 0)
      return 0;

    fprintf(out,"Case #%d: ",l+1);
    for (i=0; i<2*n; i++)
      if (!sol[i])
        break;
    if (i>=n) {
      for (j=0; j<n; j++)
        fprintf(out,"%d ",map[j][i-n]);
    }
    else {
      for (j=0; j<n; j++)
        fprintf(out,"%d ",map[i][j]);
    }
    fprintf(out,"\n");
  }
  return 0;
}
