#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <math.h>
#include <stdlib.h>

using namespace std;
string PossibleGarden(int row, int col);

int main (void)
{
	string line;
	getline(cin,line);
	
	int cases = atoi(line.c_str()); // First line
	for (int i = 0; i < cases; i++)
	{
		int row, col;
		cin >> row;
		cin >> col;
		
		string result = PossibleGarden(row,col);		

		cout << "Case #" << i+1 << ": " << result << endl;
	}	

	return 0;
}

#define ITEM(mat,row,col,cols) (*(mat+row*cols+col))

string PossibleGarden(int row, int col)
{
	int *mat = (int *) malloc(sizeof(int)*row*col);

	// Mat Init
	for (int i = 0; i < row; i ++)
		for (int j = 0; j < col; j++)
			cin >> ITEM(mat,i,j,col);

	// Test: cada altura más baja tiene que estar en una línea recta de borde a borde
	for (int height = 1; height <= 100; height++)
	{
		for (int i = 0; i < row; i ++)
			for (int j = 0; j < col; j++)
			{
				if (ITEM(mat,i,j,col) == height)
				{
					bool ver,hor;
					ver = hor = true;

					// Horizontal
					for (int k = 0; k < col; k++)
						if (ITEM(mat,i,k,col) > height)
							hor = false;

					// Vertical
					for (int k = 0; k < row; k++)
						if (ITEM(mat,k,j,col) > height)
							ver = false;

					if ((ver == false) && (hor == false))
					{
						free(mat);
						return "NO";
					}
				}
			}
	}
	free(mat);
	return "YES";
}
