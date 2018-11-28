#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
  ofstream fout("lawnmower.out");
  ifstream fin("B-small-attempt0.in");
  int width, height, times, smallest;
  fin >> times;
  bool success, colum, row; 

  for (int h = 1; h <= times; h++)
    {
      fin >> height >> width;
      int lawn[height][width];
      for (int a = 0; a < height; a++)
	for (int b = 0; b < width; b++)
	  fin >> lawn[a][b];
      
      success = true;

      for (int i = 1; i < 101; i++)
	for (int j = 0; j < height; j++)
	  for (int k = 0; k < width; k++)
	    {
	      if (lawn[j][k] == i)
		{
		  colum = true;
		  row = true;
		  for (int l = 0; l < height; l++)
		    if (lawn[l][k] > i)		      
		      colum = false;
		  if (colum == true)
		    for (int l = 0; l < height; l++)
		      lawn[l][k] = 0;
		  for (int m = 0; m < width; m++)
                    if (lawn[j][m] > i)
		      row = false;
                  if (row == true)
                    for(int m = 0; m < width; m++)
		      lawn[j][m] = 0;
		  if (!colum && !row)
		    {
		      success = false;
		    }
		}
	    }
      if (success)
	fout << "Case #" << h << ": YES" << endl;
      else fout << "Case #" << h << ": NO" << endl;
    } 
  
}
