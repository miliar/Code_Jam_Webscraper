#include <iostream>
using namespace std;

int main()
{
	int inputs;
	string input;
	string original;
	char o;

	cin >> inputs;

	for(int i = 0; i < inputs; i++)
	{
		cin >> original;

		input = original[0];

		o = input[0];

		for(int j = 1; j < original.length(); j++)
		{
			if(o > original[j])
			{
				input = input + original[j];
			}
			else
			{
				input = original[j] + input;
			}
			o = input[0];
		}

		cout << "Case #" << i+1 << ": " << input << endl;
	}
	return 0;
}