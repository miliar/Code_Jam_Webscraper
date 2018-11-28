
#include <iostream>
#include <sstream>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <stdio.h>
#include <fstream>
using namespace std;

bool checkPossibility(vector< vector<int> > startBoard,vector< vector<int> > board,int m, int n, int max)
{
	if(n<2 || m <2)
		return true;
	for(int i = 0 ; i < n; i++)
	{
		bool check = false;
		for(int j = 1 ; j < m; j++)
		{
			if(board[i][j-1]!=board[i][j])
			{
				check = true;
				break;
			}
		}
		if(!check)
		{
			startBoard[i] = vector<int>(m,board[i][0]);
		}
	}
	for(int i = 0 ; i < m; i++)
	{
		bool check = false;
		for(int j = 1 ; j < n; j++)
		{
			if(board[j-1][i]!=board[j][i])
			{
				check = true;
				break;
			}
		}
		if(!check)
		{
			for(int j = 0 ; j < n; j++)
			{
				if(startBoard[j][i]>board[j][i])
					startBoard[j][i]=board[j][i];
			}
		}
	}
	for(int i = 0 ; i < n; i++)
	{
		if(startBoard[i] != board[i])
			return false;
	}
	return true;
}
int main () 
{
  fstream fin;
  fstream fout;
  fin.open("B-small-attempt1.in",ios::in);
  fout.open("B-small-attempt0.out",ios::out);

  int N,M,T;
  fin>>T;
  int temp;
  int maxNum = -1, minNum = 101;
  vector< vector<int> > board, startBoard;
  vector<int> row;
  for(int i = 0 ; i < T; i++)
  {
	  fin>>N>>M;
	  for(int k = 0 ; k < N; k++)
	  {
		  for(int j = 0 ; j < M ; j++)
		  {
			  fin>>temp;
			  maxNum = max(maxNum,temp);
			  minNum = min(minNum,temp);
			  row.push_back(temp);
		  }
		  board.push_back(row);
		  row.clear();
	  }
	  for(int k = 0; k < N; k++)
	  {
		  startBoard.push_back(vector<int>(M,maxNum));
	  }
	  if(checkPossibility(startBoard,board,M, N, maxNum))
		  fout<<"Case #"<<i+1<<": YES\n";
	  else
		  fout<<"Case #"<<i+1<<": NO\n";
	  board.clear();
	  startBoard.clear();
  }

  fout.close();
  fin.close();
  return 0;
}