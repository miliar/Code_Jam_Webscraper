#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		string mystring;
		cin >> mystring;
		int length = mystring.length();
		char array[length];
		for (int j = 0; j < length; j++)
		{
			array[j] = mystring[j];
		}

		cout << "Case #" << i+1 << ": ";

		vector<int> put;

		char max = mystring[length-1];
		char maxlocation = length-1;

		for (int j = length-1; j >= 0; j--)
		{
			if (mystring[j] > max)
			{
				max = mystring[j];
				maxlocation = j;
			}
		}	

		cout << mystring[maxlocation];
		put.push_back(maxlocation);

		int lastput = maxlocation;


		while (lastput != 0)
		{
			char max = mystring[lastput - 1];
			char maxlocation = lastput - 1;

			for (int j = lastput-1; j >= 0; j--)
			{
				if (mystring[j] > max)
				{
					max = mystring[j];
					maxlocation = j;
				}
			}	

			lastput = maxlocation;
			put.push_back(maxlocation);
			cout << mystring[maxlocation];
		}

		int iterator = put.size() - 1;
		int finished = 0;


		for (int i = 0; i < length; i++)
		{
			if (i < put[iterator] || (finished == 1) )
			{
				cout << mystring[i];
			}
			else
			{
				if (iterator == 0)
				{
					finished = 1;	
				}

				if (finished == 0)
				{
					iterator -= 1;
				}
				
				
			}
		}

		cout << endl;


	}

}