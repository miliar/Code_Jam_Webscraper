
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <limits>
#include <iomanip>

using namespace std;
ifstream fin("b.in");
ofstream fout("b.out");


unsigned int matrix[100][100];
unsigned int rowMax[100];
unsigned int colMax[100];


bool solve(unsigned int n, unsigned int m)
{
	bool			res; 
	unsigned int	i;
	unsigned int	j;

	//row
	for(i=0;i<n;i++)
	{
		rowMax[i] = matrix[i][0];

		for(j=1;j<m;j++)
		{
			if (rowMax[i]< matrix[i][j])
			{
				rowMax[i] = matrix[i][j];
			}
		}
	}

	//col
	for(i=0;i<m;i++)
	{
		colMax[i] = matrix[0][i];

		for(j=1;j<n;j++)
		{
			if (colMax[i]< matrix[j][i])
			{
				colMax[i] = matrix[j][i];
			}
		}
	}

	//check
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if ((matrix[i][j]<rowMax[i])&&(matrix[i][j]<colMax[j]))
			{
				return false;
			}
		}
	}

	return true;
	
}



void main2(unsigned int testNum)
{
	unsigned int	i;
	unsigned int	j;
	unsigned int	n;
	unsigned int	m;
	bool			res;

	fin>>n>>m;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			fin>>matrix[i][j];
		}
	}

	res = solve(n,m);
	fout<<"Case #"<<testNum<<": "<<(res?"YES":"NO")<<endl;
}

int main(void)
{
	unsigned int numOfTests;
	unsigned int i;

	fin>>numOfTests;
	for(i=0;i<numOfTests;i++)
	{
		main2(i+1);
	}
	return 0;
}
