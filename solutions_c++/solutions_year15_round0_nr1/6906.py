#include <iostream>
#include <fstream>
#include <string>
#include <Windows.h>

using namespace std;



void main()
{
	string input[1000];
	string nums = "0123456789";
	int num[1000];
	int times;
	int counter=0;
	int counter2 = 0;
	cin >> times;

	for (int loop = 0; loop < times; loop++)
	{
		cin >> num[loop];
		cin >> input[loop];
	}

	for (int loop = 0; loop < times; loop++)
	{
		cout << "Case #" << loop + 1 << ": ";
		counter = 0;
		counter2 = 0;
		for (int step = 0; step < input[loop].length(); step++)
		{
			for (int i = 0; i < nums.length(); i++)
			{
				if (input[loop][step] == nums[i])
				{
					if (i == 0)
					{
						if (counter2>0)
						{
							counter2--;
						}
						else
						{
							counter++;
						}
					}
					if (i > 1)
					{
						counter2 = counter2 + i - 1;
					}
				}
			}
		}
		cout << counter << endl;
	}

	

	system("pause");
};