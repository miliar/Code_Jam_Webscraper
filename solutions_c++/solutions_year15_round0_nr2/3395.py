#include<iostream>
#include<fstream>

using namespace std;
int main()
{
	int T = 1;
	int sum = 0;
	int max = 0;
	int min;
	int count = 1;
	int people_num;
	int *cake;
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	fin >> T;
	while (T)
	{
		fin >> people_num;
		cake = new int[people_num];
		for (int i = 0; i < people_num; i++)
		{
			fin >> cake[i];
			if (max < cake[i])
			{
				max = cake[i];
			}
		}
		min = max;
		for (int i = 1; i < max; i++)
		{
			sum = i;
			for (int j = 0; j < people_num; j++)
			{			
				if (cake[j]>i)
				{
					if (cake[j] % i == 0)
					{
						sum += cake[j] / i - 1;
					}
					else
					{
						sum += cake[j] / i;
					}
				}
			}
			if (min > sum)
			{
				min = sum;
			}
		}
		
		fout << "Case #" << count << ": " << min << endl;
		T--;
		count++;
		delete[] cake;
	}
	system("pause");
}