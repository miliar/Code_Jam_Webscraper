#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main ()
{
	int cases=0;
	int sum[10]={0};
	char grid[4][5];
	string str;
	fstream file("A-large.in",ios::in);
	if(!file)
		exit(0);
	else
	{
		file>>cases;
		int i=0;
		
		for(i;i < cases ; i++)
		{
			int j=0;
			int sumi=0;
			for(sumi;sumi<10;sumi++)
				sum[sumi]=0;
			sumi=0;
			bool dotFound = false;
			for(j = 0; j < 4; j++)
			{
				file>>grid[j];
			}
			j=0;
			for(j = 0; j < 4; j++)
			{
				if (grid[j][0] != '.' && grid[j][1] != '.' &&  grid[j][2] != '.' && grid[j][0] != '.')
					sum[sumi++] = grid[j][0] + grid[j][1] + grid[j][2] + grid[j][3];
				else
					dotFound = true;
			}
			j=0;
			for(j = 0; j < 4; j++)
			{
				if (grid[0][j] != '.' && grid[1][j] != '.' &&  grid[2][j] != '.' && grid[3][j] != '.')
					sum[sumi++] = grid[0][j] + grid[1][j] + grid[2][j] + grid[3][j];
				else
					dotFound = true;
			}
			
			if (grid[0][0] != '.' && grid[1][1] != '.' &&  grid[2][2] != '.' && grid[3][3] != '.')
				sum[sumi++] = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3];
			else
				dotFound = true;
			
			if (grid[0][3] != '.' && grid[1][2] != '.' &&  grid[2][1] != '.' && grid[3][0] != '.')
				sum[sumi++] = grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0];
			else
				dotFound = true;
	
			int y=0;
			bool test= false;
			for (y;y <= sumi;y++)
			{
				if (sum[y] == 352)
				{
					str = "X won";
					test= true;
					break;
				}
				if (sum[y] == 348)
				{
					str = "X won";
					test= true;
					break;
				}
				if (sum[y] == 316)
				{
					str = "O won";
					test= true;
					break;
				}
				if (sum[y] == 321)
				{
					str = "O won";
					test= true;	
					break;
				}
			}
			if (test == false)
				if (dotFound == true)
					str = "Game has not completed";
				else
					str = "Draw";
			fstream outfile("ProblemA_results.txt",ios :: out | ios :: app);
			if (!file)
				exit(0);
			else
			{
				outfile<<"Case #"<<i+1<<": "<<str<<endl;
			}
			outfile.close();
		}

	}
	system("Pause");
	return 0;
}