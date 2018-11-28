#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cmath>
#include <string>

using namespace std;

#define FORI(i,n) for(int i = 0; i < n; i++)
#define FORD(i,n) for(int i = n; i >= 0; i--)

char grid[4][4];

string algo()
{
	// check rows
	vector<char> s;
	string sorted = "";
	for(int k = 0; k < 4; k++)
	{
		for(int i = 0; i < 4; i++)
		{
			s.push_back(grid[k][i]);
		}
		
		sort(s.begin(), s.end());
		
		for(int i = 0; i < 4; i ++)
		{
			sorted = sorted + s[i];
		}
		
		if(sorted == "OOOT" || sorted == "OOOO")
		{
			return "O won";
		}
		else if(sorted == "TXXX" || sorted == "XXXX")
		{
			return "X won";
		}
		
		s.clear();
		sorted = "";
	}
	
	// check columns
	for(int k = 0; k < 4; k++)
	{
		for(int i = 0; i < 4; i++)
		{
			s.push_back(grid[i][k]);
		}
		
		sort(s.begin(), s.end());
		
		for(int i = 0; i < 4; i ++)
		{
			sorted = sorted + s[i];
		}
		
		if(sorted == "OOOT" || sorted == "OOOO")
		{
			return "O won";
		}
		else if(sorted == "TXXX" || sorted == "XXXX")
		{
			return "X won";
		}
		
		s.clear();
		sorted = "";
	}
	
	// check diagonals
	s.clear();
	sorted = "";
	
	s.push_back(grid[0][0]);
	s.push_back(grid[1][1]);
	s.push_back(grid[2][2]);
	s.push_back(grid[3][3]);
	
	sort(s.begin(), s.end());
	
	for(int i = 0; i < 4; i ++)
	{
		sorted = sorted + s[i];
	}
	
	if(sorted == "OOOT" || sorted == "OOOO")
	{
		return "O won";
	}
	else if(sorted == "TXXX" || sorted == "XXXX")
	{
		return "X won";
	}
	
	s.clear();
	sorted = "";
	
	s.push_back(grid[0][3]);
	s.push_back(grid[1][2]);
	s.push_back(grid[2][1]);
	s.push_back(grid[3][0]);
	
	sort(s.begin(), s.end());
	
	for(int i = 0; i < 4; i ++)
	{
		sorted = sorted + s[i];
	}
	
	if(sorted == "OOOT" || sorted == "OOOO")
	{
		return "O won";
	}
	else if(sorted == "TXXX" || sorted == "XXXX")
	{
		return "X won";
	}
	
	// check if complete
	int m = 0, n = 0;
	FORI(m,4)
	{
		FORI(n, 4)
		{
			if(grid[m][n] == '.')
			{
				return "Game has not completed";
			}
		}
	}
	
	return "Draw";
}

int main(int argc, char** argv)
{
	int i = 0;
	int j = 0;
	int n = 4;
	
	int N = 0;
	
	cin  >> N;
	int cas = 0;
	FORI(cas, N)
	{
	
		FORI(i, n)
		{
			FORI(j, n)
			{
				cin >> grid[i][j];
			}
		}
		
		string verdict = algo();
	
		cout << "Case #" << (cas + 1)<< ": " << verdict << endl;
	}
	return EXIT_SUCCESS;
}
