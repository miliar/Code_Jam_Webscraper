#include<iostream>
#include<fstream>
using namespace std;

char*writeSummary(int width, int height, int **selection);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		int** selection;
		int height = 0;
		int width = 0;
		myfileIn >> width;
		myfileIn >> height;
		selection = new int*[width];
		for(int x = 0; x < width; x++)
		{
			selection[x] = new int[height];
			for(int y = 0; y < height; y++)
			{	
				myfileIn >> selection[x][y];
			}
		}
		myfileOut << "Case #" << (i+1) << ": " << writeSummary(width, height, selection) << endl;
		cout << "Case #" << (i+1) << ": " << writeSummary(width, height, selection) << endl;
		for(int x = 0; x < width; x++)
		{
			delete [] selection[x];
		}
		delete [] selection;
	}

	return 0;
}

char*writeSummary(int width, int height, int **selection)
{
	for(int x = 0; x < width; x++)
	{
		for(int y = 0; y < height; y++)
		{
			bool vert = (selection[x][y] >= selection[0][y] && selection[x][y] >= selection[(width-1)][y]);
			for(int xx = 1; xx < (width-1); xx++)
			{
				if(vert && selection[x][y] >= selection[xx][y])
				{
					vert = true;
				}
				else
				{
					vert = false;
					break;
				}
			}
			bool horiz = (selection[x][y] >= selection[x][0] && selection[x][y] >= selection[x][(height-1)]);
			for(int yy = 1; yy < (height-1); yy++)
			{
				if(horiz && selection[x][y] >= selection[x][yy])
				{
					horiz = true;
				}
				else
				{
					horiz = false;
					break;
				}
			}
			if(!vert && !horiz)
			{
				return "NO";
			}
		}
	}
	return "YES";
}