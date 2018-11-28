#include <iostream>
#include <fstream> 
#include <string>

using namespace std;
 
int main()
{
	int testCases;
	int count = 0;
	string input;

	ofstream out;
	out.open ("C://Users/kim/Desktop/output2.txt");
	ifstream in;
	in.open("input2.txt");
 
	in >> testCases;
 
	for (int i = 0; i < testCases; i++)
	{
		in >> input;

		out << "Case #" << i + 1 << ": ";

		int size = input.size();
		int p, count = 0;

		while (1)
		{
			p = 0;

			for (p; p<size; p++)
			{
				if (input[p] != '+')
					break;
			}

			if (p == size)
			{
				out << count << "\n";
				break;
			}

			else
			{
				char tmp = input[0];

				for (int j=0; j < size; j++)
				{
					if (tmp == input[j])
					{
						if (input[j] == '-')
							input[j] = '+';
						else
							input[j] = '-';
					}
					else
						break;
				}
				count++;
			}
		}
	}
}