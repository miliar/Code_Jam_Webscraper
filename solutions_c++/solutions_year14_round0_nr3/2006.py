#include <fstream>
#include <iostream>

using namespace std;

#define DEBUG 1

int second[100][100];
int r, c, m;

void clear(void)
{
	for (int i=0; i<100; i++)
		for(int j=0; j<100; j++)
		{
			second[i][j] = 0;
		}
}

int mymax = -1;

int test(int j, int k, int empty, int code)
{
	int s = 0;
	if (code > mymax) mymax = code;
	if (empty == 0)
		return 1;

	for(int jj = -1; jj <= 1; jj++)
		for(int kk=-1; kk<=1; kk++)
		{
			if (jj == 0 && kk == 0)
				continue;
			int new_j = j + jj;
			int new_k = k + kk;

			if (new_j >=0 && new_j<r &&
					new_k >=0 && new_k<c && second[new_j][new_k] == 0)
			{
				s++;
				second[new_j][new_k] = code;
			}
		}

	if ( s == empty) //success
		return 1;
	if (s == 0)
		return 0;
	if (s < empty)
	{
		for(int jj = -1; jj <= 1; jj++)
		{
			for(int kk=-1; kk <=1; kk++)
			{
				if (jj==0 && kk==0)
					continue;

				int new_j = j + jj;
				int new_k = k + kk;
				if (new_j >=0 && new_j<r &&
					new_k >=0 && new_k<c)
				{
					if (test(new_j, new_k, empty - s, code+1))
						return 1;
				}
			}
		}
	}

	for(int jj = -1; jj <= 1; jj++)
		for(int kk=-1; kk<=1; kk++)
		{
			if (jj == 0 && kk == 0)
				continue;
			int new_j = j + jj;
			int new_k = k + kk;

			if (new_j >=0 && new_j<r &&
					new_k >=0 && new_k<c && second[new_j][new_k] == code)
			{
				second[new_j][new_k] = 0;
			}
		}

	return 0;

}

int main()
{
	ofstream output;
	ifstream input ("C-small-attempt0.in");
	output.open("C-small-attempt0.out");

	int t;

	input >> t;

	for (int i=0; i<t; i++)
	{
		output << "Case #"<<i+1<<":"<<endl;

		input>>r>>c>>m;
		clear();

		int found = 0;
		for (int j=0; j<r && found == 0; j++)
		{
			for(int k=0; k<c && found == 0; k++)
			{
				int empty = r*c - m;
				second[j][k] = 1;
				if (test(j, k, empty - 1 , 1))
				{
					found = 1;
					//print out the result
					for(int x = 0; x < r; x++)
					{
						for(int y = 0; y < c; y++)
						{
							if (x==j && y==k)
								output<<"c";
							else if (second[x][y] == 0)
								output<<"*";
							else
								output<<".";
						}
						output<<endl;
					}
				}
				second[j][k] = 0;
			}
		}
		if (found == 0)
			output<<"Impossible"<<endl;
	}
		cout << mymax;
	return 0;
}





		


