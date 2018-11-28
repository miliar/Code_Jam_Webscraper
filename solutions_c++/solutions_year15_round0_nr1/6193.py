#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifile ("proL.in");
	ofstream ofile("resultL.out");	
	int cases = 0, dataset = 0, count = 0, sum = 0;
	char str[1010];

	ifile >> cases;
	
	for (int i = 0; i < cases; i++)
	{
		ifile >> dataset;
		ifile.getline(str, 10100);
		for (int j = 1; str[j] != NULL; j++)
		{
			sum += str[j] - 48;
			if (str[j] == '0' && sum < j)
			{
				count++;
				sum++;
			}
		}

		ofile << "Case #" << i + 1 << ": " << count << '\n';
		count = 0;
		sum = 0;
	}

	return 0;
}