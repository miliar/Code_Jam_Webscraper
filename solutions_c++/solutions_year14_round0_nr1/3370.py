#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int T = 0;
	fin >> T;
	for(int t = 1; t <= T;t++)
	{
	int a[4], b[4];
	int row1 = 0, row2 = 0, tmp = 0;
	fin >> row1;
	for(int i = 0;i < 4;i++)
	{
		for(int j = 0;j < 4;j++)
		{
			if(i == row1 - 1)
				fin >> a[j];
			else
				fin >> tmp;
		}
	}
	
	fin >> row2;
	for(int i = 0;i < 4;i++)
	{
		for(int j = 0;j < 4;j++)
		{
			if(i == row2 - 1)
				fin >> b[j];
			else
				fin >> tmp;
		}
	}
	bool flag = false, cheat = false;
	int num = 0;
	for(int i = 0;i < 4;i++)
	{
		for(int j = 0;j < 4;j++)
		{
			if(a[i] == b[j])
			{
				if(flag == false)
				{
					flag = true;
					num = a[i];
				}
				else
				{
					cheat = true;
				}
			}
		}
	}

	fout << "Case #" <<t << ": ";
	if(cheat)
	{
		fout << "Bad magician!";
	}
	else
	{
		if(flag)
		{	
			fout << num;
		}
		else
		{
			fout << "Volunteer cheated!";
		}
	}

	if(t != T)
		fout << endl;
}

	return 0;
}