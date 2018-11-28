#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int firstData[4][4]={0};
	int secondData[4][4]={0};
	int num=0;

	ifstream fin("C:\\Users\\yanglv\\Desktop\\A-small-attempt0.in");
	ofstream fout("result.txt");

	fin>>num;

	for (int i=1;i<=num;i++)
	{
		int firstIndex=0,secondIndex=0;

		fin>>firstIndex;
		firstIndex--;

		//input the data matrix
		for (int r=0;r<4;r++)
		{
			for (int c=0;c<4;c++)
			{
				fin>>firstData[r][c];
			}
		}

		fin>>secondIndex;
		secondIndex--;

		for (int r=0;r<4;r++)
			for (int c=0;c<4;c++)
				fin>>secondData[r][c];

		//judge
		int commonCount=0,value=0;

		for (int j=0;j<4;j++)
		{
			for (int k=0;k<4;k++)
			{
				if (firstData[firstIndex][j] == secondData[secondIndex][k])
				{
					commonCount++;
					value = firstData[firstIndex][j];
					break;
				}
			}
		}

		if (commonCount == 1)
		{
			fout<<"Case #"<<i<<": "<<value<<endl;
		}
		else if (commonCount >1)
		{
			fout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else if (commonCount == 0)
		{
			fout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
	}

	return 0;
}