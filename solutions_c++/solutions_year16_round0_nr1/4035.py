
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
//official solution

using namespace std;

ifstream fin("..//A-large.in");
ofstream fout("..//A-large.out");

int T;
int N;


int is_finish(int find10[])
{
	for (int i = 0; i < 10; i++)
	{
		if (find10[i] == 0) return 0;
	}
	return 1;
}


int main()
{
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		int flag = 0;
		int find10[10] = { 0 };
		fin >> N;
		if (N == 0)
		{
			fout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}
		for (int j = 1; j<N * 200; j++)
		{
			int culculate_N = N*j;
			while (culculate_N > 0)
			{
				int remine_num;
				remine_num = culculate_N % 10;
				find10[remine_num] = 1;
				culculate_N = culculate_N / 10;
			}
			if (is_finish(find10))
			{
				flag = 1;
				fout << "Case #" << i << ": " << N*j << endl;
				break;
			}
		}
		if (flag == 0)
		{
			fout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		
		
	}
	

	return 0;
}







