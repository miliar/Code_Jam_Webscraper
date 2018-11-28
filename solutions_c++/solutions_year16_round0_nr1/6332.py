#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

bool check(bool b[])
{
	for (int i = 0; i < 10; i++)
		if (b[i] == false)
			return false;
	return true;
}

int main()
{
	ifstream in;
	in.open("C:\\Users\\ãÍãÏ\\Desktop\\A-large.in");
	ofstream out;
	out.open("C:\\Users\\ãÍãÏ\\Desktop\\out.txt");

	bool numbers[10];
	

	int str;
	in >> str;
	int numberOfTestCases =str;
	long long number, i;

	for (int caseNumber = 1; caseNumber <= numberOfTestCases; caseNumber++)
	{
		in >> str;
		number = str;

		for (int q = 0; q < 10; q++)
			numbers[q] = false;

		if (number != 0)
		{
			i = 1;
			while (true)
			{
				while (number!=0)
				{
					int index = number % 10;
					numbers[index] = true;
					number/=10;
				}

				if (check(numbers) == true)
				{
					out << "Case #" << caseNumber << ": " << str*i << endl;
					break;
				}

				number = str * (i + 1);
				i++;
			}

		}
		else
		{
			out << "Case #" << caseNumber << ": INSOMNIA" << endl;
		}

	}

	in.close();
	out.close();
	//system("pause");
}