#include <iostream>
#include <fstream>
#include <set>
#include <vector>
using namespace std;

void main()
{
	std::ifstream ifs ("input.txt", std::ifstream::in);
	int tests;
	ifs>>tests;
	ofstream myfile;
	myfile.open ("output.txt");
	for(int i=0;i<tests;i++)
	{
		set<int> candidates;
		//First instance
		{
			int row;
			ifs>>row;
			for(int j=1;j<=4;j++)
			{
				for(int k=1;k<=4;k++)
				{
					int temp;
					ifs>>temp;
					if(j == row)
					{
						candidates.insert(temp);
					}
				}
			}
		}
		//Second Instance
		{
			int row;
			ifs>>row;
			int count = 0;
			vector<int> results(4);
			for(int j=1;j<=4;j++)
			{
				for(int k=1;k<=4;k++)
				{
					int temp;
					ifs>>temp;
					if(j == row)
					{
						if(candidates.find(temp)!=candidates.end())
						{
							results[count] = temp;
							count++;
						}
					}
				}
			}
			myfile << "Case #"<<(i+1)<<": ";
			if(count == 0)
			{
				myfile << "Volunteer cheated!";
			}
			else if(count > 1)
			{
				myfile << "Bad magician!";
			}
			else
			{
				myfile << results[0];
			}
			myfile<<"\r\n";
		}
	}
	ifs.close();
	myfile.close();
}