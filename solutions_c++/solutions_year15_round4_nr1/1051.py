#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
using namespace std;
#define LEFT 1
#define RIGHT 2
#define UP 3
#define DOWN 4

int A[100][100];
int R, C;

int has_arrow(int r, int c, int rp, int cp) {
  //printf("(%d,%d)\n", r,c);
  while(r+rp<R && c+cp<C && r+rp>=0 && c+cp>=0) {
    r+=rp;
    c+=cp;
    //printf("A[%d][%d]=%d\n", r,c,A[r][c]);
    if(A[r][c])
      return 1;
  }
  return 0;
}

int check(int r, int c) {
  if(A[r][c]==0)
    return 1;
  if(A[r][c]==RIGHT) {
    if(has_arrow(r,c,0,1))
      return 1;
  }
  else if(A[r][c]==LEFT) {
    if(has_arrow(r,c,0,-1))
      return 1;
  }
  else if(A[r][c]==UP) {
    if(has_arrow(r,c,-1,0))
      return 1;
  }
  else if(A[r][c]==DOWN) {
    if(has_arrow(r,c,1,0))
      return 1;
  }
  int arrow_switch = has_arrow(r,c,0,1) | has_arrow(r,c,0,-1) |
    has_arrow(r,c,1,0) | has_arrow(r,c,-1,0);
  if(arrow_switch)
    return 0;
  return -1;
  
}


int main() {

  int T;
  scanf("%d", &T);
  
  for(int i=0; i<T; i++) {
    scanf("%d %d", &R, &C);
    for(int j=0; j<R; j++) {
      char buff[102];
      scanf("%s", buff);
      for(int k=0; k<C; k++) {
	if(buff[k]=='.') {
	  A[j][k]=0;
	}
	else if(buff[k]=='<')
	  A[j][k]=LEFT;
	else if(buff[k]=='^')
	  A[j][k]=UP;
	else if(buff[k]=='v')
	  A[j][k]=DOWN;
	else
	  A[j][k]=RIGHT;
	//printf("%d", A[j][k]);
      }
      //printf("\n");
    }
    
    int ans = 0;
    int flag = 0;
    for(int j=0; j<R; j++) {
      for(int k=0; k<C; k++) {
	int ret = check(j,k);
	//printf("%d..", has_arrow(j,k,1,0));
	//printf("%d", ret);
	if(ret==-1)
	  flag = -1;
	if(ret==0)
	  ans++;
      }
      //printf("\n");
    }
    printf("Case #%d: ", i+1);
    if(flag==-1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", ans);
  }

  return 0;

}
