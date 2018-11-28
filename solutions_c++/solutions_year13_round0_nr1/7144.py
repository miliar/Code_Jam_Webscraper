#include <iostream>
#include <fstream>

#define INFILE "C:\\GCJ\\CodeJam\\input_output\\A-large.in"
#define OUTFILE "C:\\GCJ\\CodeJam\\input_output\\Alarge.out"
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open(INFILE);
	if(!fin.is_open())
	{
		cout<<"Failed to open input file. Press a key to exit...";
		cin.get();
		return 0;
	}
	fout.open(OUTFILE);
	if(!fin)
	{
		cout<<"Failed to open output file. Press a key to exit...";
		cin.get();
		return 0;
	}	
	// Actual code starts
	//===================
	int totalcases = 0;
	fin>>totalcases;
	
	cout<<"\nReading total cases: "<<totalcases;

	for(int c = 1; c <= totalcases; c++)
	{
		bool blankLeft = false;
		fin.get();
		fout<<"Case #"<<c<<": ";
		bool concluded = false;

		char grid[4][4];
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				grid[i][j] = fin.get(); 
				if('.' == grid[i][j])
					blankLeft = true;
			}
			fin.get();
		}

		// parse the rows
		for(int i=0; i<4; i++)
		{
			bool same = true;
			int start = 1;
			char prev = grid[i][0];
			
			if(prev == 'T')
			{
				prev = grid[i][1];
				start++;			
			}
			if(prev == '.')
			{
				continue;
			}
			for(int j=start; j<4; j++)
			{
				if(grid[i][j] != prev && grid[i][j] != 'T')
				{
					same = false;
					break;
				}
			}
			if(same)
			{
				fout<<prev<<" won\n";
				concluded = true;
				break;
			}
		}

		if(concluded)
			continue;

		// parse the columns
		for(int j=0; j<4; j++)		
		{
			bool same = true;
			int start = 1;
			char prev = grid[0][j];			
			if(prev == 'T')
			{
				prev = grid[1][j];
				start++;			
			}
			if(prev == '.')
			{				
				continue;
			}

			for(int i=start; i<4; i++)
			{
				if(grid[i][j] != prev && grid[i][j] != 'T')
				{
					same = false;
					break;
				}
			}
			if(same)
			{
				fout<<prev<<" won\n";
				concluded = true;
				break;
			}
		}

		if(concluded)
			continue;

		// Parse the two diagonals
		do
		{
			bool same = true;
			char prev = grid[0][0];
			int start = 0;
			if(prev == 'T')
			{
				prev = grid[1][1];
				start++;			
			}
			if(prev == '.')
			{
				break;
			}
			for(int i=start, j=start; i<4; i++,j++)
			{
				if(grid[i][j] != prev && grid[i][j] != 'T')
				{
					same = false;
					break;
				}
			}
			if(same)
			{
				fout<<prev<<" won\n";
				concluded = true;					
			}
			
		}while(0);

		if(concluded)
			continue;
		do
		{
			bool same = true;
			char prev = grid[3][0];
			int start = 1;

			if(prev == 'T')
			{
				prev = grid[2][1];
				start++;			
			}
			if(prev == '.')
			{
				break;
			}
			for(int i= 3 - start, j=start; j<4; i--,j++)
			{
				if(grid[i][j] != prev && grid[i][j] != 'T')
				{
					same = false;
					break;
				}
			}
			if(same)
			{
				fout<<prev<<" won\n";
				concluded = true;					
			}

		}while(0);


		if(!concluded)
		{
			if(blankLeft)
			{
				fout<<"Game has not completed\n";
			}
			else
			{
				fout<<"Draw\n";
			}
		}
	}


	//===================
	// Actual code ends
	if(fin)
	{
		fin.close();
	}
	if(fout)
	{
		fout.close();
	}
	cout<<"\nExiting program. Press a key to exit...";
	cin.get();
	return 0;
}