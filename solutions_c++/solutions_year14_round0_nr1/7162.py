#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int t;
	ofstream fout;
	ifstream fin;
	
	fout.open("A-small-attempt3.out");
	fin.open("A-small-attempt3.in");
	fin >> t;
	int array[4][4];
	int sarray[4][4];
	int answer = -1;
	int ans[t];
	int a1, a2;
	for(int i = 0; i < t; i++)
	{
		fin >> a1;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				fin >> array[j][k];
			}
		}
		fin >> a2;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				fin >> sarray[j][k];
			}
		}
		for(int j = 1; j <= 16; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				for(int l = 0; l < 4; l++)
				{
					if(array[a1-1][k] == j && sarray[a2-1][l] == j)
					{
						if(answer == -1)
						{
							answer = j;
						}
						else if(answer > 0)
						{
							answer = 0;
							break;
						}
					}
				}
			}
		}
		ans[i] = answer;
		a1 = 0;
		a2 = 0;
		answer = -1;
	}
	
	for(int i = 0; i < t; i++)
	{
		fout << "Case #" << i+1 << ": ";
		if(ans[i] == 0)
		{
			fout << "Bad Magician!" << endl;
		}
		else if(ans[i] == -1)
		{
			fout << "Volunteer Cheated!" << endl;
		}
		else
		{
			fout << ans[i] << endl;
		}
	}
	
	fout.close();
	fin.close();

	return 0;
}