#include<iostream>
#include<cstdio>
#include<string>
#include<vector>

using namespace std;

bool solve(vector<vector<int> > &, int, int);

int main()
{
  int t = 0;
  cin >> t;
  
  for (int i = 0; i < t; ++i)
  {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int> > lawn(n, vector<int>(m, 0));
    
    for(int i = 0; i < n; ++i )
    {
      for ( int j = 0; j < m; ++j)
      {
	cin >> lawn[i][j];
      }
    }
    
    printf("Case #%d: %s\n", i+1, solve(lawn, n, m)? "YES":"NO");
  }
  
  return 0;
}

bool possible(vector<vector<int> > & lawn, int i, int j, int n, int m)
{
  bool line = true, row = true;
  
  for(int k = 0; k < n; ++k)
  {
    if(lawn[k][j] > lawn[i][j])
    {
      row = false;
      break;
    }
  }
  
  for(int l = 0; l < m; ++l)
  {
    if (lawn[i][l] > lawn[i][j])
    {
      line = false;
      break;
    }
  }
  return line || row;
}

bool solve(vector<vector<int> > & lawn, int n, int m)
{
  for(int i = 0; i < n; ++i)
  {
    for(int j = 0; j < m; ++j)
    {
      if(!possible(lawn, i, j, n, m))
	return false;
    }
  }
  return true; 
}