#include<iostream>
#include<cstdio>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<cstdlib>
#include<utility>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include <string>
#include <vector>
#include<fstream>
using namespace std;

int t,n,m,A[500][500],MAX_row[500],MAX_col[500];

int main()
{
      ifstream fin("input.txt"); ofstream fout("output.txt"); 
  bool flag=0;
  fin >> t;
  int c=0;
  while(t--)
  {
    memset(MAX_col,0,sizeof(MAX_col));
    memset(MAX_row,0,sizeof(MAX_row));
    flag=0;
    c++;
    fin >> n >> m;
    for(int i=0;i<n;i++)
    {
      for(int j=0;j<m;j++)
      {
	fin >> A[i][j];
	if(MAX_row[i]<A[i][j]) MAX_row[i]=A[i][j];
      }
    } 
      for(int j=0;j<m;j++)
      {
	for(int i=0;i<n;i++)
	{
	  if(A[i][j]>MAX_col[j]) MAX_col[j]=A[i][j];
	}
      }
      
      for(int i=0;i<n;i++)
      {
	for(int j=0;j<m;j++)
	{
	  if(MAX_col[j]>A[i][j]&&MAX_row[i]>A[i][j]) {flag=1;break;}
	}
	if(flag)break;
      }
      if(flag) fout << "Case #"<<c<<": NO"<<endl;
      else fout << "Case #"<<c<<": YES"<<endl;
    
  }
  return 0;
}
