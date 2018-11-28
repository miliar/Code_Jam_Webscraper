//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

const int MAXN = 100;

int t;
int n, m;
char grid[MAXN + 3][MAXN + 3];
int rows[MAXN + 3], columns[MAXN + 3];

void Read(){
  scanf("%d %d", &n, &m);
  for(int i=0; i<n; i++)
    scanf("%s", grid[i]);
}

void Clean(){
  for(int i=0; i<n; i++)
    rows[i] = 0;
  for(int j=0; j<m; j++)
    columns[j] = 0;
}

int Solve(){
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(grid[i][j] != '.')
	rows[i]++, columns[j]++;
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(grid[i][j] != '.' && rows[i] == 1 && columns[j] == 1)
	return -1;
      
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(grid[i][j] != '.'){
	if(grid[i][j] == '<')
	  grid[i][j] = '#';
	break;
      }
  for(int i=0; i<n; i++)
    for(int j=m-1; j>=0; j--)
      if(grid[i][j] != '.'){
	if(grid[i][j] == '>')
	  grid[i][j] = '#';
	break;
      }
  for(int j=0; j<m; j++)
    for(int i=0; i<n; i++)
      if(grid[i][j] != '.'){
	if(grid[i][j] == '^')
	  grid[i][j] = '#';
	break;
      }
  for(int j=0; j<m; j++)
    for(int i=n-1; i>=0; i--)
      if(grid[i][j] != '.'){
	if(grid[i][j] == 'v')
	  grid[i][j] = '#';
	break;
      }
   
  int ret = 0;
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(grid[i][j] == '#')
	ret++;
      
  return ret;
}

int main(){
  scanf("%d", &t);
  for(int pp=1; pp<=t; pp++){
    Read();
    int res = Solve();
    if(res == -1)
      printf("Case #%d: IMPOSSIBLE\n", pp);
    else
      printf("Case #%d: %d\n", pp, res);
    Clean();
  }
  
  return 0;
}