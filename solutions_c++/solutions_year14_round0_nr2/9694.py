#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

void Input(fstream& myfile, int* arr, int n);
double Count(double C, double F, int farm);
double Min(double* arr, int n);

void main()
{
	fstream myfile;
	myfile.open("B-small-attempt2.in", fstream::in);
	ofstream output("Output.in");

	if (myfile.is_open() || !myfile.eof()) {

			int times, count = 1;

			myfile >> times;

			while (count <= times)
			{
				double C, F, X, solution, threshold, *arr;
				int tr, i = 0, j = 0;
				
				myfile >> C;
				myfile >> F;
				myfile >> X;

				tr = (int)(X / C);
				threshold = X / 2.0;

				arr = new double[tr + 1];
			
				do
				{
					solution = Count(C, F, i);
					solution = solution + X / (F * i + 2.0);
					if (solution <= threshold)
					{
						arr[j] = solution;
						j++;
					}
					i++;

				} while (i <= tr);

				output << fixed << setprecision(7) << showpoint;
				output << "Case #" << count << ": " << Min(arr, j) << endl;

				count = count + 1;

				delete[] arr;
			}
	}

	myfile.close();
	output.close();
}

double Count(double C, double F, int farm)
{
	double time = 0.0, each;

	if (farm == 0)
		return time;
	else {
		for (int i = 0; i < farm; i++)
		{
			each = 2.0 + i * F;
			time = time + C / each;
		}

		return time;
	}
}

void Input(fstream& myfile, int* arr, int n)
{
	for (int i = 0; i < n; i++)
	{
		myfile >> *(arr + i);
		cout << *(arr + i);
	}
}

double Min(double* arr, int n)
{
	int mi = 0;

	for (int i = 0; i < n; i++)
	{
		if (arr[i] < arr[mi])
		{
			mi = i;
		}
	}

	return arr[mi];
}