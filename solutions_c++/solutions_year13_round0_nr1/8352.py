#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int row_judge(char *map)
{
	int i, j, flag, t= -1;
	for(i = 0; i < 4; i++)
	{
		flag = 0;
		if(map[i * 4] != '.')
		for(flag = 1, j = 0; j < 3; j++)
		{
			if(map[i * 4 + j] == 'T')
			{
				t = i * 4 + j;
				map[i * 4 + j] = map[i * 4 + j + 1];
				if(map[i * 4 + j + 1] == '.')
				{
					flag = 0;
					break;
				}
			}
			if(map[i * 4 + j + 1] == 'T')
			{
				t = i * 4 + j + 1;
				map[i * 4 + j + 1] = map[i * 4 + j];
			}
			if(map[i * 4 + j] != map[i * 4 + j + 1])
			{
				flag = 0;
				break;
			}
		}
		if(flag)
		{
			return map[i * 4 + j];
		}
	}
	if(t >= 0)
	map[t] = 'T';
	return -1;
}
int col_judge(char *map)
{
	int i, j, flag, t = -1;
	for(i = 0; i < 4; i++)
	{
		flag = 0;
		if(map[i + j * 4] != '.')
		for(flag = 1, j = 0; j < 3; j++)
		{
			if(map[i + j * 4] == 'T')
			{
				t = i + j * 4;
				map[i + j * 4] = map[i + (j + 1) * 4];
				if(map[i + (j + 1) * 4] == '.')
				{
					flag = 0;
					break;
				}
			}
			if(map[i + (j + 1) * 4] == 'T')
			{
				t = i + (j + 1) * 4;
				map[i + (j + 1) * 4] = map[i + j * 4];
			}
			if(map[i + j * 4] != map[i + (j + 1) * 4])
			{
				flag = 0;
				break;
			}
		}
		if(flag)
		{
			return map[i + 4 * j];
		}
	}
	if(t >= 0)
	map[t] = 'T';
	return -1;
}
int x_judge(char *map)
{
	int i, j, flag;
	if(map[0] == '.')
	flag = 0;
	else
	for(i = 0, flag = 1; i < 15; i += 5)
	{
		if(map[i] == 'T')
		{
			map[i] = map[i + 5];
			if(map[i] == '.')
			{
				flag = 0;
				break;
			}
		}
		if(map[i + 5] == 'T')
		{
			map[i + 5] = map[i];
		}
		if(map[i] != map[i + 5])
		{
			flag = 0;
			break;
		}	
	}
	if(flag)
	{
		return map[i];
	}
	if(map[3] == '.')
	flag = 0;
	else
	for(i = 3, flag = 1; i < 12; i += 3)
	{
		if(map[i] == 'T')
		{
			map[i] = map[i + 3];
			if(map[i] == '.')
			{
				flag = 0;
				break;
			}
		}
		if(map[i + 3] == 'T')
		{
			map[i + 3] = map[i];
		}
		if(map[i] != map[i + 3])
		{
			flag = 0;
			break;
		}
	}
	if(flag)
	{
		return map[i];
	}
	return -1;
}
int notyet_judge(char *map)
{
	int i;
	for(i = 0; i < 16; i++)
	{
		if(map[i] == '.')
		return 1;
	}
	return 0;
}
int main()
{
	char map[16], flag;
	int i, j, t, finish;
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt1.in");
	fout.open("A-small-attempt1.out");
	fin >> t;
	fin.get();
	finish = 1;
	while(t--)
	{	
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				fin >> map[i * 4 + j];
			}
			fin.get();
		}
		fin.get();
		if((flag = row_judge(map)) > 0)
		{
			fout << "Case #" << finish << ": " << flag << " won\n";
		}
		else if((flag = col_judge(map)) > 0)
		{
			fout << "Case #" << finish << ": " << flag << " won\n";
		}
		else if((flag = x_judge(map)) > 0)
		{
			fout << "Case #" << finish << ": " << flag << " won\n";
		}
		else if((flag = notyet_judge(map)) > 0)
		{
			fout << "Case #" << finish << ": Game has not completed\n";
		}
		else
		{
			fout << "Case #" << finish <<": Draw\n";
		}
		finish++;
	}
	fin.close();
	fout.close();
	return 0;
}