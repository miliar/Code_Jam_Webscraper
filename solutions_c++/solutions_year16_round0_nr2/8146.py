#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

bool check(string& line)
{
	bool valid = true;
	for (size_t i = 0; i < line.size(); i++)
	{
		if (line[i] != '+')
		{
			valid = false;
			break;
		}
	}

	return valid;
}

void flip(string& line, int length)
{
	char fchar = line[0];
	
	if (fchar == '+')
	{
		int i = 0;
		while (fchar == line[i])
			i++;
		

		for (size_t j = 0; j < i; j++)
		{
			line[j] = '-';
		}
		/*for (size_t k = 0; k < length; k++)
			cout << line[k] << " ";
		cout << endl;*/
	}
	else
	{
		int i = 0;
		while (fchar == line[i])
			i++;
			
		for (size_t j = 0; j < i; j++)
		{
			line[j] = '+';
		}

		/*for (size_t k = 0; k < length; k++)
			cout << line[k] << " ";
		cout << endl;*/
	}
	
}

int main()
{
	int T;
	cin >> T;

	int CASE = 1;
	cin.ignore();

	while (T--)
	{
		string line = "";
		getline(cin, line);
		int flipCount = 0;
		
		if (check(line) == true)
		{
			cout << "Case #" << CASE << ": " << 0 << endl;
		}
		else
		{
			
			while (check(line) != true)
			{
				flip(line, line.size());
				flipCount++;
			}

			cout << "Case #" << CASE << ": " << flipCount << endl;
		}
		
		
		CASE++;
	}

	return 0;
}