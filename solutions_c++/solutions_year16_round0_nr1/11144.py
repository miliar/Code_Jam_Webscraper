#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;


int main()
{
	int cases;
	cin >> cases;
	int *caseNum = new int[cases];
	for (int i = 0; i < cases; i++)
	{
		cin >> caseNum[i];
	}
	for (int c = 0; c < cases; c++)
	{
		bool seenNumbers[10] = { false };
		int input = caseNum[c];
		string number;
		if (input != 0)
		{
			for (int i = 1; ; i++)
			{
				int result = i * input;
				number = to_string(result);//itoa(result, number.c_str(), 10);
				for (int x = 0; x < number.length(); x++)
				{
					int tempNum = number[x] - '0';
					seenNumbers[tempNum] = true;
				}
				bool tempBool;
				for (int x = 0; x < 10; x++)
				{
					if (!seenNumbers[x])
					{
						tempBool = false;
						break;
					}
					else
					{
						tempBool = true;
					}
				}
				if (tempBool)
				{
					break;
				}
			}
		}
		if(input == 0)
		{
			cout << "Case #" << c+1 << ": INSOMNIA" << endl;
		}
		else
		{
			cout << "Case #" << c+1 << ": " << number << endl;
		}
	}
	cin.get();
	cin.get();
}