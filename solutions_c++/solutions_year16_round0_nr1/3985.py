#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	bool zero = false;
	bool one = false;
	bool two = false;
	bool three = false;
	bool four = false;
	bool five = false;
	bool six = false;
	bool seven = false;
	bool eight = false;
	bool nine = false;

	int number;
	//cin >> number;

	ifstream ifs("A-large.in");
	ifs >> number;

	int case_number = 0;

input:
	while(ifs >> number)
	{
		string result;
		case_number++;

		for(int i = 1; i < 1000000; i++)
		{
			result = to_string(number*i);

			for(int j = 0; j < result.size(); j++)
			{
				if(result[j] == '0')
				{
					zero = true;
				}
				if(result[j] == '1')
				{
					one = true;
				}
				if(result[j] == '2')
				{
					two = true;
				}
				if(result[j] == '3')
				{
					three = true;
				}
				if(result[j] == '4')
				{
					four = true;
				}
				if(result[j] == '5')
				{
					five = true;
				}
				if(result[j] == '6')
				{
					six = true;
				}
				if(result[j] == '7')
				{
					seven = true;
				}
				if(result[j] == '8')
				{
					eight = true;
				}
				if(result[j] == '9')
				{
					nine = true;
				}

				if(zero && one && two && three && four && five && six && seven && eight && nine)
				{
					cout << "Case #" << case_number << ": " << result << endl;
					zero = false;
					one = false;
					two = false;
					three = false;
					four = false;
					five = false;
					six = false;
					seven = false;
					eight = false;
					nine = false; 
					goto input;
				}
			}
		}
		if(!(zero && one && two && three && four && five && six && seven && eight && nine))
		{
			cout << "Case #" << case_number << ": INSOMNIA" << endl;
			zero = false;
			one = false;
			two = false;
			three = false;
			four = false;
			five = false;
			six = false;
			seven = false;
			eight = false;
			nine = false; 
			goto input;
		}
	}

	return 0;	
}



