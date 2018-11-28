#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

bool IsOk(vector<vector<char>> &m, int R, int C, int i, int j)
{
  switch(m[i][j])
  {
  case '.':
    return true;
  case '<':
    j--;
    while(j>=0)
    {
      if(m[i][j]=='.')
        j--;
      else
        return true;
    }

    return false;

  case '>':
    j++;
    while(j<C)
    {
      if(m[i][j]=='.')
        j++;
      else
        return true;
    }

    return false;

  case '^':
    i--;
    while(i>=0)
    {
      if(m[i][j]=='.')
        i--;
      else
        return true;
    }

    return false;

  case 'v':
    i++;
    while(i<R)
    {
      if(m[i][j]=='.')
        i++;
      else
        return true;
    }

    return false;
  }
}

bool CanChange(vector<vector<char>> &m, int R, int C, int i, int j)
{
  int ti=i, tj=j;

  j--;
  while(j>=0)
  {
    if(m[i][j]=='.')
      j--;
    else
    {
      m[ti][tj]='<';
      return true;
    }
  }

  i=ti; j=tj;
  j++;
  while(j<C)
  {
    if(m[i][j]=='.')
      j++;
    else
    {
      m[ti][tj]='>';
      return true;
    }
  }

  i=ti; j=tj;
  i--;
  while(i>=0)
  {
    if(m[i][j]=='.')
      i--;
    else
    {
      m[ti][tj]='^';
      return true;
    }
  }

  i=ti; j=tj;
  i++;
  while(i<R)
  {
    if(m[i][j]=='.')
      i++;
    else
    {
      m[ti][tj]='v';
      return true;
    }
  }

  return false;
}

int main()
{
  int T;

  //ifstream in("test.in");
  //ofstream out("test.out");

  //ifstream in("A-small-attempt2.in");
  //ofstream out("A-small-attempt2.out");

  ifstream in("A-large.in");
  ofstream out("A-large.out");

  in >> T;

  for(int testCase=0; testCase<T; ++testCase)
  {
    int solve = 0; 

    int R,C;

    in >>R >>C;

    vector<vector<char>> m(R,vector<char>(C));

    for(int i=0; i<R;i++)
      for(int j=0; j<C; j++)
        in >> m[i][j];

    bool isOk = true;

    for(int i=0; i<R;i++)
    {
      for(int j=0; j<C; j++)
      {
        if(!IsOk(m,R,C,i,j))
        {
          if(!CanChange(m,R,C,i,j))
          {
            isOk=false;
            break;
          }
          else
            solve++;
        }
      }
      if(!isOk)
        break;
    }

    if(isOk)
      for(int i=0; i<R;i++)
      {
        for(int j=0; j<C; j++)
        {
          if(!IsOk(m,R,C,i,j))
            cout  << "Bug!" << endl;
        }
      }
    
    out << "Case #"<<testCase+1<<": ";

    if(isOk)
      out << solve << endl;
    else
      out << "IMPOSSIBLE" << endl;
  }

  return 0;
}