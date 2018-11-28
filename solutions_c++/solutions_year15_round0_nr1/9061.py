#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int res, cases, stoodUp, maxS;
	string shyness;
	cin >> cases;
	
	for (int i = 1; i <= cases; i++)
	{
		res = 0;
		cin >> maxS >> shyness;
		stoodUp = (int)shyness[0] - (int)'0';
		for (int j = 1; j < shyness.size(); j++)
		{
			if (shyness[j] != '0')
			{
				if (stoodUp >= j)
				{
					stoodUp += (int)shyness[j] - (int)'0';
				}
				else
				{
					res += j - stoodUp;
					stoodUp = j + (int)shyness[j] - (int)'0';
				}
			}
		}
		cout << "Case #" << i << ": " << res << endl;
	}	
}