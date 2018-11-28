#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
using namespace std;
string grid[200];
int r,c;
int testrow(int row){
  int tot = 0;
  for(int j =0;j<c; j++){
    if(grid[row][j] !='.')
      tot++;
      
  }
  if(tot > 1)
    return 1;
  else
    return -1;
}

int testcol(int col){
  int tot =0;
  for(int i = 0; i  <r;i++){
    if(grid[i][col] !='.')
      tot++;
  }
  if(tot > 1)
    return 1;
  else
    return -1;
}

int minrow(int row){

  for(int j = 0; j < c; j++){
    if(grid[row][j]!='.')
      return j;

  }
  return -1;
}
int maxrow(int row){
  for(int j = c-1;j >=0; j--){
    if(grid[row][j]!='.')
      return j;
  }
  return -1;
}

int mincol(int col){
  for(int i = 0; i < r;i++){
    if(grid[i][col] !='.')
      return i;
  }
  return -1;
}
int maxcol(int col){

  for(int i = r-1; i >=0;i--){
    if(grid[i][col] !='.')
      return i;
  }
  return -1;
}

void work()
{
  cin >> r >> c;
  for(int i =0;i <r;i++)cin >> grid[i];
  for(int i = 0; i < r; i++)
    for(int j = 0; j < c; j++){
      if(grid[i][j] !='.' && testrow(i)<0 and testcol(j) < 0){
	printf("IMPOSSIBLE\n");
	return;
      }
    }
  int res = 0;
  for(int i=0; i < r; i++ ){
    int x = minrow(i), y= maxrow(i);
    if(x<0)
      continue;
    if( x==y){
      if(grid[i][x]=='<' || grid[i][x]=='>')
	res++;
    }
    else{
      if(grid[i][x]=='<')
	res++;
      if(grid[i][y]=='>')
	res++;
    }
  }
  for(int j=0;j <c;j++){
    int x = mincol(j), y =maxcol(j);
    if(x<0)
      continue;
    if(x==y){
      if(grid[x][j]=='^' ||grid[x][j] =='v')
	res++;
    }
    else {
      if(grid[x][j] =='^')
	res++;
      if(grid[y][j] =='v')
	res++;
    }
  }
  printf("%d\n",res);

}
int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <=T;i++){
    printf("Case #%d: ", i);
    work();
  }

}
