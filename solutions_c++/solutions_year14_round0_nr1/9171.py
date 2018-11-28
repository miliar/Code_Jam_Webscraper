#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;



int main()
{

	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	int n;
	in >> n;

	int n1;
	int arr1[4][4];
	int n2;
	int arr2[4][4];


	int l = 0;
	int m;

	for (int i = 1; i <= n; i++)
	{
		in >> n1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				in >> arr1[j][k];
			}

		in >> n2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				in >> arr2[j][k];
			}

		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				if (arr1[n1 - 1][j] == arr2[n2 - 1][k])
				{
					l++;
					m = arr1[n1 - 1][j];
				}

				if (l == 2)
					break;
			}

		if (l == 1)
		{
			out << "Case #" << i << ": " << m << endl;
		}
		else if (l == 0)
		{
			out << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		}
		else
		{
			out << "Case #" << i << ": " << "Bad magician!" << endl;
		}

		l = 0;

	}

	return 0;
}
