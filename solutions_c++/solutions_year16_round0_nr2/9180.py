#include<stack>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

bool check(string arr)
{
	for (int i = 0;i < arr.size();i++)
	{
		if (arr[i] != '+')
			return false;
	}
	return true;
}

void main()
{
	fstream f;
	fstream file;
	f.open("B-large.in");

	int tCases;
	f >> tCases;
	file.open("output.txt", ios::app);
	//cout << "hello";

	int count = 0;

	string input = "";
	

	
	int i = 1;
	for (i;i <= tCases;i++)
	{
		f >> input;
		count = 0;
		if (check(input))
		{
			
			file << "Case #" << i << ": " << count << endl;
			continue;

		}

		for (int m = input.size();m > -1;m--)
		{
			if (input[m] == '-')
			{
				count++;
				for (int j = 0;j <= m;j++)
				{
					if (input[j] == '+')
						input[j] = '-';
					else
						input[j] = '+';
				}
				if (check(input))
				{
					
					file << "Case #" << i << ": " << count << endl;
					break;
				}


			}
		}
	}
	
}
