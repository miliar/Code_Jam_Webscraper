#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void main()
{
	ifstream input;
	input.open("A-large.in");

	if (!input.is_open())
	{
		cout << "Error opening file\n";
		system("pause");
	}

	int tot_cases;
	input >> tot_cases;

	ofstream output;
	output.open("solution.out");

	for (int i = 0; i < tot_cases; i++)
	{
		output << "Case #" << i + 1 << ": ";

		int smax = 0;
		int add_friend = 0;
		input >> smax;
		string data;
		input >> data;
		int total = data[0] - '0';

		for (int j = 1; j < smax+1; j++)
		{
			if (total >= j)
			{
				total = total + data[j] - '0';
			}
			else
			{
				add_friend = add_friend + (j - total);
				total = total + (j - total);
				total = total + data[j] - '0';
			}
		}

		output << add_friend << '\n';
	}

	output.close();
	input.close();
}