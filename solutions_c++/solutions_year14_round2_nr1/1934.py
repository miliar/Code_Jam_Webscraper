#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int i, r;
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t;
	fin >> t;


	int n; 
	char data[200][200];
	int curIndex[200];
	int count[200];
	float sum;
	char ch;
	int result;
	bool fail;
	
	for (int test = 0; test < t; test++)
	{
		fin >> n; 
		for (i = 0; i < n; i++)
		{
			fin >> data[i];
			curIndex[i] = 0;
		}

		result = 0;
		fail = false;

		while (1)
		{
			sum = 0;
			ch = '0';
			for (i = 0; i < n; i++)
			{
				count[i] = 0;
				for (r = curIndex[i]; r < strlen(data[i]); r++)
				{
					if (ch == '0')
						ch = data[i][r];
					else if (ch != data[i][r])
					{
						fail = true;
						break;
					}
						
					count[i]++;
					sum++;
					if (r == strlen(data[i]) - 1 || data[i][r] != data[i][r + 1])
						break;
				}
				curIndex[i] = r;
				if (curIndex[i] < strlen(data[i])) curIndex[i]++;

				if (fail)
					break;
				if (count[i] == 0)
				{
					fail = true;
					break;
				}
			}
			if (fail)
				break;
			
			int mid = (sum + 0.5) / n;
			for (i = 0; i < n; i++)
			{
				result += abs(mid - count[i]);
			}

			for (i = 0; i < n; i++)
			{
				if (curIndex[i] != strlen(data[i]))
					break;
			}
			if (i == n)
				break;
		}

		fout << "Case #" << (test + 1) << ": ";
		if (fail)
			fout << "Fegla Won" << endl;
		else
			fout << result << endl;
	}

	return 0;
}
