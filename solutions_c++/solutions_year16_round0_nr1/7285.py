
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool found(bool seenDigits[])
{
	for (int j = 0; j < 10; ++j)
	{
		if(seenDigits[j] == false)
		{
			return false;
		}
	}
	return true;
}

int main(int argc, char const *argv[])
{
	long int n;
	ifstream input ("input.txt");
	ofstream output ("output.txt");
	input >> n;

	for (long int i = 0; i < n; ++i)
	{
		long int value;
		input >> value;
		bool seenDigits[10];
		for (int j = 0; j < 10; ++j)
		{
			seenDigits[j] = false;
		}
		long int counter = 0;
		while(!found(seenDigits))
		{
			counter++;
			long int newValue = value * counter;
			while (newValue > 0) 
			{
				int digit = newValue % 10;
				seenDigits[digit] = true;
				newValue /= 10;
			}
			if(counter == 100000000)
			{
				break;
			}
		}
		if(counter != 100000000)
		{
			output << "Case #" << i+1 << ": " << value * counter << endl;
			cout << "Case #" << i+1 << ": " << value * counter << endl;
		}
		else
		{
			output << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		}

	}
	return 0;
}