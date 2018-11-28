#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
	int N;
	int choice;
	int Matrix[4][4];
	
	int first[4];
	int second[4];

	int count = 1;
	
	int result[100];
	
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt3.in");
	fout.open("output");
	fin >> N;
	while (count <= N)
	{
		fin >> choice;
		choice--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> Matrix[i][j];
			}
		}
		
		for (int i = 0; i < 4; i++)
		{
			first[i] = Matrix[choice][i];
		}

		fin >> choice;
		choice--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> Matrix[i][j];
			}
		}

		for (int i = 0; i < 4; i++)
		{
			second[i] = Matrix[choice][i];
		}


		//compare first and second
		choice = 4;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (first[i] == second[j])
				{
					if (choice == 4)
					{
						choice = i;
					}
					else
					{
						result[count-1] = -1;
						choice = -1;
					}
				}
			}
		}

		if (choice == 4)
		{
			result[count-1] = -2;
		}
		else if (choice != -1)
		{
			result[count-1] = first[choice];
		}
		count++;
	}

	for (int i = 0; i < N; i++)
	{
		if (i != 0)
		{
			fout<<endl;
		}

		fout<<"Case #"<<i+1<<": ";
		switch (result[i])
		{
			case -1:fout<<"Bad magician!";break;
			case -2:fout<<"Volunteer cheated!";break;
			default:fout<<result[i];break;
		}
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
