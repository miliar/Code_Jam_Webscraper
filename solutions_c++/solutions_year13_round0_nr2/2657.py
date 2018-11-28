#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

#define PI M_PI

double dist(int x, int y)
{
  return sqrt(x*x+y*y);
}

int main()
{
	ifstream input;
	string line;
	char *tstr;
	int T;

	int gin[100][100];
	int grid[2][100][100];
	int val;
	int N, M;
	int min, max;
	int i, j, k;
	int oe, a, b;
	bool ans;
    bool exchange;

	//input.open("sample.in");
	input.open("B-small-attempt2.in");
	//input.open("B-large.in");

	getline(input, line);

	T = atoi(line.c_str()); /* 1 <= T <= 100 */

	for(int run=1; run<=T; run++)
	{
		input >> N;
		input >> M;
		
		min = 100;
		max = 0;
		for(i=0; i<N; i++)
		{
			for(j=0; j<M; j++)
			{
				input >> val;
				
				if(val < min)
					min = val;
					
				if(val > max)
					max = val;
					
				gin[i][j] = val;
			}
		}
		
		for(i=0; i<N; i++)
		{
			for(j=0; j<M; j++)
			{
				grid[0][i][j] = grid[1][i][j] = gin[i][j];
			}
		}

//		X = (N > M) ? N : M;
//		Y = (N < M) ? N : M;

	    ans = true;
	        
        for(k=min; k<max; k++)
        {
			a = k%2;
			b = (k+1)%2;
			
			for(i=0; i<N; i++)
			{
				exchange = true;
				for(j=1; j<M; j++)
				{
					if(grid[a][i][j] != grid[a][i][0])
					{
						exchange = false;
						j = M;
					}
				}
				if(exchange)
				{
					for(j=0; j<M; j++)
					{
						grid[b][i][j] = grid[a][i][0]+1;
						//cout << grid[b][i][j];
					}
					//cout<<endl;
				}
			}
			
			for(j=0; j<M; j++)
			{
				exchange = true;
				for(i=1; i<N; i++)
				{
					if(grid[a][i][j] != grid[a][0][j])
					{
						exchange = false;
						i = N;
					}
				}
				if(exchange)
				{
					for(i=0; i<N; i++)
					{
						grid[b][i][j] = grid[a][0][j]+1;
						//cout << grid[b][i][j];
					}
					//cout<<endl;
				}
			}
			
			for(i=0; i<N; i++)
			{
				for(j=0; j<M; j++)
				{
//					cout << grid[b][i][j];
					if(grid[b][i][j] == k)
					{
						ans = false;
					}
				}
//				cout<<endl;
			}
//			cout<<endl;
		}
		
		if(ans)
		{
			cout << "Case #" << run << ": YES" << endl;
		}
		else
		{
			cout << "Case #" << run << ": NO" << endl;
		}
	}
	
	return 0;
}
