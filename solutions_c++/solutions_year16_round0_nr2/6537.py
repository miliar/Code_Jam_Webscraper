#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");

	int cases;
	in >> cases;
	
	for (int i = 1; i <= cases; i++)
	{
		string input;
		in >> input;

		char current = ' ';
		int change = 0;

		for (int j = 0; j < input.length(); j++)
		{
			if (input[j] != current)
			{
				change++;
				current = input[j];
			}
		}
		if (current == '+')
		{
			change--;
		}
		out << "Case #" << i << ": " << change << endl;
	}
}