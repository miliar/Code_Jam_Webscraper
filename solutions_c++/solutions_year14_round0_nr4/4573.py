#include <iostream>
#include <fstream>

using namespace std;

void quickSort(double data[], int low, int high);

int main()
{
	ifstream inFile;
	ofstream outFile;
	int T, N;
	int scoreWar, scoreDeWar;
	double *NaomiBlocks, *KenBlocks;
	int caseIndex, NaomiIndex, KenIndex, i;

	inFile.open("E:\\C++\\GCJ\\Google Code Jam 2014\\Qualification Round\\D Deceitful War\\D-large.in");
	outFile.open("E:\\C++\\GCJ\\Google Code Jam 2014\\Qualification Round\\D Deceitful War\\D-large.out");

	inFile >> T;
	for (caseIndex = 1; caseIndex <= T; caseIndex++)
	{
		inFile >> N;
		NaomiBlocks = new double [N];
		KenBlocks = new double [N];

		for (i = 0; i < N; i++)
		{
			inFile >> NaomiBlocks[i];
		}
		for (i = 0; i < N; i++)
		{
			inFile >> KenBlocks[i];
		}
		quickSort(NaomiBlocks, 0, N);
		quickSort(KenBlocks, 0, N);

		for (i = 0; i < N; i++)
		{
			cout << NaomiBlocks[i] << '\t';
		}
		cout << endl;
		for (i = 0; i < N; i++)
		{
			cout << KenBlocks[i] << '\t';
		}
		cout << endl;

		for (NaomiIndex = N - 1, KenIndex = N - 1, scoreDeWar = 0; KenIndex >= 0; KenIndex--)
		{
			if (NaomiBlocks[NaomiIndex] > KenBlocks[KenIndex])
			{
				NaomiIndex--;
				scoreDeWar++;
			}
		}

		for (NaomiIndex = N - 1, KenIndex = N - 1, scoreWar = 0; NaomiIndex >= 0; NaomiIndex--)
		{
			NaomiBlocks[NaomiIndex] < KenBlocks[KenIndex] ?
				KenIndex-- : scoreWar++;
		}

		cout << "Case #" << caseIndex << ": " << scoreDeWar << ' ' << scoreWar << endl;
		outFile << "Case #" << caseIndex << ": " << scoreDeWar << ' ' << scoreWar << endl;

		delete [] NaomiBlocks;
		delete [] KenBlocks;
	}//for (caseIndex = 1; caseIndex <= T; caseIndex++)

	inFile.close();
	outFile.close();

	system("pause");
	return 0;
}

void quickSort(double data[], int low, int high)
{
	if (high - low < 2)
	{
		return;
	}
	int i = low, j = high - 1;
	double key = data[low];

	while (i < j)
	{
		while (i < j && key < data[j])
		{
			j--;
		}
		if (i < j)
		{
			data[i++] = data[j];
		}
		while (i < j && data[i] < key)
		{
			i++;
		}
		if (i < j)
		{
			data[j--] = data[i];
		}
	}
	data[i] = key;

	quickSort(data, low, i);
	quickSort(data, i + 1, high);
}