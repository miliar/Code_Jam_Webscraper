#include <iostream>
#include <string.h>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

string flip(string sOrig, int ammount)
{
	string sSwap = sOrig.substr(0, ammount);
	string sOut;

	for (int i = 0; i < sSwap.length(); i++)
	{
		if (sSwap[i] == '+')
			sSwap[i] = '-';
		else
			sSwap[i] = '+';
	}

	for (int i = 0; i < sSwap.length(); i++)
	{
		sOut += sSwap[sSwap.length() - i - 1];
	}

	return sOut + sOrig.substr(ammount, sOrig.length() - ammount);
}

int smart_search(string sIn, int iSt)
{
	for (int i = iSt; i < sIn.length(); i++)
	{
		if (sIn[i] != sIn[iSt])
		{
			return i;
		}
		else if (i + 1 == sIn.length())
		{
			return sIn.length();
		}
	}

	return -1;
}

void print(string sIn)
{
	for (int a = 0; a < sIn.length(); a++)
	{
		if (sIn[a] == '+')
			cout << "+";
		else
			cout << "-";
	}
	cout << endl;
}

int main()
{
	long int T = 0;
	string stack;
	int iStart = 0;
	char cFirst;
	int steps;

	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		cin >> stack;

		steps = 0;

		while((iStart = stack.find_first_of("-")) != std::string::npos)
		{
			cFirst = stack[0];

			if (cFirst == '-')
			{
				iStart = smart_search(stack, iStart);
				stack = flip(stack, iStart);
				steps++;
				//print(stack);

				if ((iStart = stack.find_first_of("-")) != std::string::npos)
				{
					//iStart = smart_search(stack, '-');
					stack = flip(stack, iStart);
					steps++;
					//print(stack);
				}
			}
			else
			{
				if ((iStart = stack.find_first_of("+")) != std::string::npos)
				{
					iStart = smart_search(stack, iStart);
					stack = flip(stack, iStart);
					steps++;
					//print(stack);

					if ((iStart = stack.find_first_of("+")) != std::string::npos)
					{
						stack = flip(stack, iStart);
						steps++;
						//print(stack);
					}
				}
			}
		}

		cout << "Case #" << i << ": " << steps << endl;
	}

	getchar();
	getchar();
	return 0;
}
