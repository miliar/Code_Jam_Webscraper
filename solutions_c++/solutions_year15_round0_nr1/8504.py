#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int CalculateFriends(int shynesLevel,string people)
{
	int number = 0, friends=0, sum=0;
	char prvi;
	for (int i = 0; i < shynesLevel+1; i++)
	{
		prvi = people[i];
		number = atoi(&prvi);
		sum += number;
		if (sum < i + 1)
		{
			friends++;
			sum += 1;
		}
	}
	return friends;
}

int main()
{
	ifstream dat("A-large.in", ios::out | ios::app | ios::binary);
	ofstream output;
	output.open ("output.out");
	if (dat.is_open())
	{
		if (output.is_open())
		{
			int tests = 0, shynesLevel = 0;
			dat >> tests;
			string people;
			for (int i = 0; i < tests; i++)
			{
				people = "";
				dat >> shynesLevel;
				dat >> people;
				//string out = "Case #" + (i + 1) + ": " + CalculateFriends(shynesLevel, people) + "/n";
				output << "Case #" << i + 1 << ": " << CalculateFriends(shynesLevel, people)<<"\n";
			}
			dat.close();
			output.close();
			cout << "Results are found in file output.txt" << endl;
		}
		else
		{
			cout << "Could not create output file." << endl;
		}
	}
	else
	{
		cout << "File could not be opened. Input file must be in the same directory as source code!" << endl;
	}
	system("pause");
}