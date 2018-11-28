#include<fstream>
using namespace std;

int max1, max2, N, total;
int cArray[26];

bool findMax()
{
	if (cArray[0] < cArray[1])
	{
		max1 = 1;
		max2 = 0;
	}
	else
	{
		max1 = 0;
		max2 = 1;
	}
	for (int i = 2; i < N; i++)
	{
		if (cArray[i] > cArray[max1])
		{
			max2 = max1;
			max1 = i;
		}
		else if (cArray[i] > cArray[max2])
		{
			max2 = i;
		}
	}
	if (cArray[max1] == 0)
		return false;
	return true;
}

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");

	int T;
	char c;
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		fin >> N;
		total = 0;
		for (int j = 0; j < N; j++)
		{
			fin >> cArray[j];
			total += cArray[j];
		}
		fout << "Case #" << i + 1 << ": ";
		while (findMax())
		{
			if (cArray[max2] > (total - 2) / 2)
			{
				if (total-2==1)
				{
					cArray[max1] -= 1;
					c = 65 + max1;
					fout << c << " ";
					total -= 1;
				}
				else
				{
					cArray[max1] -= 1;
					c = 65 + max1;
					fout << c;
					cArray[max2] -= 1;
					c = 65 + max2;
					fout << c << " ";
					total -= 2;
				}
			}
			else
			{
				cArray[max1] -= 2;
				c = 65 + max1;
				fout << c << c << " ";
				total -= 2;
			}
		}
		fout << endl;
	}

	return 0;
}