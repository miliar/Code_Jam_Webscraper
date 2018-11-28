#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int findCount(int number)
{
	string numbers = "0123456789";

	int count = 0;
	int current = number;
	
	while (numbers.size() != 0)
	{
		string num = to_string(current);
		for (size_t i = 0; i < numbers.size(); i++)
		{
			size_t position = num.find(numbers[i]);
			if (position != string::npos)
			{
				numbers.erase(i, 1);
				i--;
			}
		}
		count++;
		current = number * (count + 1);
	}

	return (number * count);
}

void start()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");

	int testCases;
	in >> testCases;
	
	for (int i = 1; i <= testCases; i++)
	{
		int number;
		in >> number;

		if (number == 0)
		{
			out << "Case #" << i << ": INSOMNIA" << endl;
		}
		else
		{
			int counter = findCount(number);

			out << "Case #" << i << ": " << counter << endl;
		}
	}
}

int main()
{
	start();
}