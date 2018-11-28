#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream in(".\\input.txt");
	ofstream out(".\\output.txt");
	int T;
	in>>T;
	for (int i = 0; i < T; i++)
	{
		int first, second;
		in>>first;
		int one[4][4], two[4][4];
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				in>>one[j][k];
			}
		}
		in>>second;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				in>>two[j][k];
			}
		}
		int time = 0;
		int key;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (one[first-1][j] == two[second-1][k])
				{
					key = one[first-1][j];
					time++;
				}
			}
		}
		out<<"Case #"<<i+1<<": ";
		if (time == 0)
		{
			out<<"Volunteer cheated!"<<endl;
		}
		else if (time == 1)
		{
			out<<key<<endl;
		}
		else
		{
			out<<"Bad magician!"<<endl;
		}
	}
	return 0;
}