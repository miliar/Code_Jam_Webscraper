#include <fstream>
#include <iostream>

using namespace std;


unsigned int **lawn;
unsigned int **init;

bool checkrow(unsigned int **lawn, int x, int y, int w)
{
	int i;
	
	for(i = 0; i < w; i ++)
	{
		if(lawn[x][y] < lawn[x][i])
			return false;
	}
	return true;
}

bool checkcolumn(unsigned int **lawn, int x, int y, int h)
{
	int i;
	
	for(i = 0; i < h; i ++)
	{
		if(lawn[x][y] < lawn[i][y])
			return false;
	}
	return true;
}

bool solve(int game, int w, int h)
{
	int i, j;
	bool flag = true;

	unsigned int ih;
	
		
	for(i = 0; i < h; i ++)
	{
		for(j = 0; j < w; j ++)
		{
			if(!(checkrow(lawn, i, j, w) || checkcolumn(lawn, i, j, h)))
				return false;
		}
	}
	return true;
		
}




int main()
{
	ifstream fin;
	ofstream fout;
	
	fin.open("small2.in");
	fout.open("small.out");
	
	int n, w, h, i, j, k;
	char ch;
	
	fin >> n;
	
	for(i = 0; i < n ; i ++)
	{
		fin >> h >> w;
		
		lawn = new unsigned int*[h];
		
		for(j = 0; j < h; j ++)
		{
			lawn[j] = new unsigned int[w];
			
			for(k = 0; k < w; k ++)
			{
				fin >> lawn[j][k];
				//cout << lawn[j][k] << " ";
			}
			//cout << endl;
		}
		
		if(solve(i, w, h))
		{
			cout << "Case #" << i + 1 << ": YES\n\n";
			fout << "Case #" << i + 1 << ": YES\n";
		}
		else
		{
			cout << "Case #" << i + 1 << ": NO\n\n";
			fout << "Case #" << i + 1 << ": NO\n";
		}

		
		
		for(j = 0; j < h; j ++)
		{
			delete[] lawn[j];
		}
		
		delete[] lawn;
		
/*		for(j = 0; j < h; j ++)
		{
			delete[] init[j];
		}
		delete[] init;
*/
		
		//cout << endl;
	}
	fout << endl;
	
	
	
	fin.close();
	fout.close();
	
}
