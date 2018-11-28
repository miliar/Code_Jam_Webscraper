#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int T, N;
	int count = 1;
	int m[1000];
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> T;
	while (T)
	{
		int sumA, sumB, max_eat;
		sumA = sumB = max_eat = 0;
		fin >> N;
		for (int i = 0; i < N; i++)
		{
			fin >> m[i];
			if (i>0)
			{
				if (m[i] < m[i - 1])
				{
					sumA += m[i - 1] - m[i];
					if (m[i - 1] - m[i]>max_eat)
					{
						max_eat = m[i - 1] - m[i];
					}
				}
			}
		}
		for (int i = 0; i < N - 1; i++)
		{
			if (m[i] <= max_eat)
				sumB += m[i];
			else
				sumB += max_eat;
		}
		fout << "Case #" << count << ": " << sumA << " " << sumB << endl;
		count++;
		T--;
	}
	system("pause");
	return 0;
}