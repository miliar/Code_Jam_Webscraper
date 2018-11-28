#include <iostream>
#include <string>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++)
	{
		int count = 0;
		string input;
		cin >> input;

		char last = input[0];
		for(int j = 1; j < input.length(); j++)
		{
			if(input[j] != last)
			{
				count++;
				last = input[j];
			} 
		}
		if(last == '-')
		{
			count++;
		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}

	return 0;
}
