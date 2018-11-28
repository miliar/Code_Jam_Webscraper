#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


int grid[101][101];

int r[101];
int c[101];

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(9);
	fout.precision(9);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		
		int n,m;
		fin >> n >> m;
		memset(grid,0,sizeof(grid));
		
		for(i=0; i<n; i++)
		{
			r[i]=0;
			for(j=0; j<m; j++)
			{
				c[j]=0;
				
				fin >> grid[i][j];
			}
		}
				
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				if(grid[i][j] > r[i])
					r[i]=grid[i][j];
				if(grid[i][j]>c[j])
					c[j]=grid[i][j];
			}
		}
		bool isok = true;
		
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				if(grid[i][j] < min(r[i],c[j]))
				   isok=false;
			}
		}
		
		
		cout << "Case #" << ct << ":";
		fout << "Case #" << ct << ":";
		
		if(!isok)
		{
			cout << " NO";
			fout << " NO";
		}
		else {
			cout << " YES";
			fout << " YES";
		}
		
		
		
		fout << endl;
		cout << endl;
		
	}
	
	
	return 0;
}

