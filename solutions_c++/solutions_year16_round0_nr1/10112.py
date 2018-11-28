#include<iostream>
#include<fstream>
using namespace std;

bool SeenNumbers[10];


bool Check()
{
	for (int i = 0; i < 10; i++)
	{
		if (!SeenNumbers[i])
		{
			return false;
		}
	}
	return true;
}

int main() 
{
	for (int i = 0; i < 10; i++)
	{
		SeenNumbers[i] = false;
	}

	int TestCases=0;
	int Number=0;
	int multiplier = 1;
	ifstream myFile;
	ofstream result;
	result.open("output.txt");
	myFile.open("input.txt");
	myFile >> TestCases;
	int Original;
	

	if (TestCases > 100) 
	{
		cout << "Test cases too large" << endl;
		return 0;
	}


	for (int i = 0; i < TestCases; i++) 
	{
		myFile >> Number;
		Original = Number;
		for (int i = 0; i < 10; i++)
		{
			SeenNumbers[i] = false;
		}

		
		if (Number > 0) {

			while (!Check())
			{



				int temp = Number;

				while (temp > 0)
				{
					SeenNumbers[temp % 10] = true;
					temp /= 10;

				}

				if (Check())
				{
					result << "Case #"<<i+1<<": "<< Number << endl;
					multiplier = 1;
				}
				else
				{
					multiplier++;
					Number = Original*multiplier;
					

				}
			}
		}
		else 
		{
			result << "Case #" << i+1 << ": INSOMNIA"<< endl;
		}

	}


	myFile.close();
	result.close();
	system("pause");

	return 0;
}

