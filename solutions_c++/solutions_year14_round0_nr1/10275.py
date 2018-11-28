#include <iostream>
#include <fstream>

using namespace std;
void readFile();
int findIntersection(int row1[], int row2[]);

int main(int argc, char *argv[]) 
{
	readFile();
}

void readFile()
{
	ifstream f;
	f.open("input.txt");
	
	ofstream of;
	of.open("output.txt");
	
	int cases = 0;
	int case_count = 1;
	int row1_data[4];
	int row2_data[4];
	
	int dump = 0;
	
	f>>cases;
	while(!f.eof())
	{
		int row1 = -1;
		int row2 = -1;
		
		f>>row1;
		for(int i=1; i<=4; i++)
		{
			for(int j=1; j<=4; j++)
			{
				if(i==row1)
				{
					 f>>row1_data[j-1];
				}
				else
				{
					f>>dump;
				}
			}
		}
		
		//Similarly for row2
		f>>row2;
		for(int i=1; i<=4; i++)
		{
			for(int j=1; j<=4; j++)
			{
				if(i==row2)
				{
					 f>>row2_data[j-1];
				}
				else
				{
					f>>dump;
				}
			}
		}
		
		//Now find intersection
		int match = 0;
		int magic_number = -1;
		for(int i = 0; i<4; i++)
		{
			for(int j = 0; j<4; j++)
			{
				if(row1_data[i] == row2_data[j])
				{
					match++;
					magic_number = row1_data[i];
				}
			}
		};
		
		if(match == 0)
		{
			//Volunteer Cheater
			of<<"Case #"<<case_count<<": Volunteer cheated!\n";
		}
		else if(match == 1)
		{
			of<<"Case #"<<case_count<<": "<<magic_number<<"\n";
		}
		else
		{
			of<<"Case #"<<case_count<<": Bad magician!\n";
		}
		
		case_count++;
	}
}