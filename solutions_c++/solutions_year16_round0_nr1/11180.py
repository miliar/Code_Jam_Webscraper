#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int total, listcount = 0;
	//vector<long long unsigned int> number;
	long long unsigned number, number_copy;
	unsigned int insomania;
	vector<int> seen(10, 0);
	unsigned int seenIndex = 0, SingleNumCount = 0;

	cin >> total;
	while (total != 0)
	{
		listcount++;
		insomania = 0;
		cin >> number;
		number_copy = number;

		SingleNumCount = 0;
		while(SingleNumCount < 100000)
		{
			insomania = 0; 
			while (number_copy != 0)
			{
				seenIndex = number_copy % 10;
				number_copy = number_copy / 10;
				seen[seenIndex] = 1;
			}
			SingleNumCount++;
			for (int i = 0; i < 10; i++)
			{
				if (seen[i] == 0)
				{
					insomania = 1;
				}
			}
			if (insomania)
			{
				number_copy = number*SingleNumCount;
				insomania = 0;
			}
			else
			{
				number_copy = number*(SingleNumCount - 1);
				break;
			}
		}
		for (int i = 0; i < 10; i++)
		{
			if (seen[i] == 0)
			{
				insomania = 1;
			}
		}
		cout << "Case #" << listcount << ": ";
		if (insomania == true)
		{
			cout << "INSOMNIA" << endl;
		} 
		else
		{
			cout << number_copy << endl;

		}
		total--;
		for (int i = 0; i < 10; i++)
		{
			seen[i] = 0;
		
		}
	}
}