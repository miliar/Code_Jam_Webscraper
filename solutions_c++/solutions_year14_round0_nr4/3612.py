#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void main()
{
	int T,N,k, WarCount=0, D_WarCount=0;
	char line[10000], digit[10];

	ifstream ifile("D-large.in");
	ofstream ofile("output.out");

	ifile.getline(line,10000);

	T = atoi(line);
	for (int testCase = 1; testCase <= T; testCase++)
	{
		WarCount = 0, D_WarCount = 0;

		ifile.getline(line, 10000);
		N = atoi(line);

		double *box_N = new double[N];
		double *box_K = new double[N];

		ifile.getline(line, 10000);
		for (int i = 0, index = 0; index < N; i++, index++)
		{
			for (k = 0; line[i] != ' ' && line[i] != '\0'; k++, i++)
			{
				digit[k] = line[i];
			}
			i++;
			digit[k] = '\0';
			box_N[index] = atof(digit);
		}

		ifile.getline(line, 10000);
		for (int i = 0, index = 0; index < N; i++, index++)
		{
			for (k = 0; line[i] != ' ' && line[i] != '\0'; k++, i++)
			{
				digit[k] = line[i];
			}
			i++;
			digit[k] = '\0';
			box_K[index] = atof(digit);
		}

		for (int i = 0; i < N; i++)
		{
			for (k = i; k < N; k++)
			{
				if (box_N[k] < box_N[i])
					swap(box_N[i], box_N[k]);
				if (box_K[k] < box_K[i])
					swap(box_K[i], box_K[k]);
			}
		}


		k = 0;
		for (int i = 0; i < N; i++)
		{
			if (box_N[i]>box_K[k])
			{
				D_WarCount++;
				k++;
			}
		}

		k = 0;
		for (int i = 0; i < N; i++)
		{
			if (box_K[i]>box_N[k])
				k++;
			else
				WarCount++;
		}
		delete box_N;
		delete box_K;

		ofile << "Case #" << testCase << ": ";
		ofile << D_WarCount << " " << WarCount << endl;
	}
}