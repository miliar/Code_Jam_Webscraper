#include<iostream>
#include<fstream>
#include<string>
using namespace std;



int main()
{
	ifstream input("A-large.in");
	ofstream output("output.txt");
	int T;
	int len;
	string digit;

	input >> T;

	for (int i = 0; i < T; i++)
	{
		input >> len >> digit;

		int amount = 0;
		int invited = 0;
		for (int j = 0; j <= len; j++)
		{
			int current = digit[j] - '0';

			if (j > amount)
			{
				invited += (j - amount);
				amount = j;
			}
			
			amount += current;
		}

		output << "Case #" << i+1 << ": " << invited << endl;
	}




	output.close();
	input.close();

	return 0;
}