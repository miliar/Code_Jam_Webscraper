#include <iostream>
#include <fstream>

using namespace std;

void main() 
{
	int arr[5] = {1, 4, 9, 121, 484};

	ifstream input_file ("input_file.txt");
	ofstream output_file ("output_file.txt");
	int kamut;

	int count, a, b;

	input_file >> kamut;

	for (int i = 0; i < kamut; i++)
	{
		count = 0;
		input_file >> a >> b;
		
		for (int j = 0; j < 5; j++)
		{
			if (arr[j] >= a && arr[j] <= b)
			{
				count++;
			}
		}

		output_file << "Case #" << i+1 << ": " << count << endl;
	}

	input_file.close();
	output_file.close();
}