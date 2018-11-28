#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
void main()
{
	int t, n;
	ofstream output;
	output.open("answer.txt");
	ifstream input;
	input.open("ques.in");
	input >> t;
	for (int i = 0; i<t; i++)
	{
		input >> n;
		int num, sample[12], k, element = 0, mul = 1, pass = 1;
		while (pass == 1)
		{
			num = n*mul;
			if (num == 0)
			{
				output << "Case #" << i + 1 << ": INSOMNIA\n";
				break;
			}
			while (num>0)
			{
				int found = 1;
				k = num % 10;
				num = num / 10;
				for (int j = 0; j<element; j++)
				{
					if (sample[j] == k)
					{
						found = 0;
					}
				}
				if (found == 1)
				{
					sample[element] = k;
					element= element+1;
				}
				if (element == 10)
				{
					output << "Case #" << i + 1 << ": " << n*mul << "\n";
					pass = 0;
					break;
				}
			}
			mul++;
		}
	}
	output.close();
	input.close();
}