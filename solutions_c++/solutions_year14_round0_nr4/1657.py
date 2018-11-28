#include <fstream>

using namespace std;

double a[1000], b[1000];

void quickSort(double arr[], int left, int right)
{
	int i = left, j = right;
	double tmp;
	double pivot = arr[(left + right) / 2];
	while (i <= j)
	{
		while (arr[i] > pivot)
				i++;
		while (arr[j] < pivot)
				j--;
		if (i <= j)
		{
			tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
			i++;
			j--;
		}
	}
	if (left < j)
		quickSort(arr, left, j);
	if (i < right)
		quickSort(arr, i, right);
}

int main(void)
{
	ofstream fout("Output.out");
	ifstream fin("Input.in");

	int Ncase, Ncurrent, n, i, i1, i2, ansA, ansB;
	
	fin >> Ncase;
	for(Ncurrent = 1; Ncurrent <= Ncase; Ncurrent++)
	{
		ansA = 0;
		ansB = 0;
		fin >> n;
		for (i = 0; i < n; i++)
			fin >> a[i];
		for (i = 0; i < n; i++)
			fin >> b[i];
		quickSort(a, 0, n-1);
		quickSort(b, 0, n-1);

		i1 = 0;
		i2 = 0;
		for (i = 0; i < n; i++)
		{
			if (a[i1] > b[i2])
			{
				ansA++;
				i1++;
				i2++;
			}
			else
				i2++;
		}

		i1 = 0;
		i2 = 0;
		for (i = 0; i < n; i++)
		{
			if (a[i1] > b[i2])
				i1++;
			else
			{
				i1++;
				i2++;
				ansB++;
			}
		}
		ansB = n - ansB;
		fout << "Case #" << Ncurrent << ": " << ansA << " " << ansB << endl;
	}

	return 0;
}
