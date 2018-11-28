#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<algorithm>

using namespace std;

int main()
{
	int count;
	cin >> count;
	for(int i=1; i<=count; i++)
	{
		int retval = 0;
		//Want +, not -

		string pancakes;
		int flipper;
		cin >> pancakes >> flipper;

		while(pancakes.find("-") != string::npos)
		{
			retval++;
			if(retval > 10000)
			{
				break;
			}
			if(retval % 2)
			{
				size_t at = pancakes.rfind("-");
				if((at - (flipper-1)) < 0)
				{
					retval = 10001;
					break;
				}
				for(int i=at-(flipper-1); i<=at; i++)
				{
					if(pancakes[i] == '-')
					{
						pancakes[i] = '+';
					}
					else
					{
						pancakes[i] = '-';
					}
				}
			}
			else
			{
				size_t at = pancakes.find("-");
				if((at + flipper) >= pancakes.size())
				{
					retval = 10001;
					break;
				}
				for(int i=at; i<(at + flipper); i++)
				{
					if(pancakes[i] == '-')
					{
						pancakes[i] = '+';
					}
					else
					{
						pancakes[i] = '-';
					}
				}
			}
		}


		cout << "Case #" << i << ": ";
		if(retval > 10000)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << retval;
		}
		cout << endl;
	}

	return 0;
}
