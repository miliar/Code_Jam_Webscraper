#include <iostream>
#include <fstream>

using namespace std;

void Input(fstream& myfile, int* arr, int n);

void main()
{
	fstream myfile;
	myfile.open("A-small-attempt1.in", fstream::in);
	ofstream output("Output.in");

	if (myfile.is_open() || !myfile.eof()) {

			int times, count = 1;

			myfile >> times;

			while (count <= times)
			{
				int first, second, found = 0, solution = 0,
					*arr1, *arr2;

				arr1 = new int[16];
				arr2 = new int[16];

				myfile >> first;
				first = first - 1;
				Input(myfile, arr1, 16);
				myfile >> second;
				second = second - 1;
				Input(myfile, arr2, 16);

				for (int i = 0; i < 4; i++)
				{
					if (found == 2)
						break;
					for (int j = 0; j < 4; j++)
					{
						if (arr1[first * 4 + i] == arr2[second * 4 + j])
						{
							found = found + 1;
							solution = arr1[first * 4 + i];
							break;
						}
					}
				}

				output << "Case #" << count << ": ";

				if (found == 0)
					output << "Volunteer cheated!" << endl;
				else if (found == 1)
					output << solution << endl;
				else
					output << "Bad magician!" << endl;

				count = count + 1;

				delete [] arr1;
				delete [] arr2;
			}
	}

	myfile.close();
	output.close();
}

void Input(fstream& myfile, int* arr, int n)
{
	for (int i = 0; i < n; i++)
	{
		myfile >> *(arr + i);
		cout << *(arr + i);
	}
}