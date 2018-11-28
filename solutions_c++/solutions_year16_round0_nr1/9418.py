#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	int tests;
	cin  >> tests;
	int number;
	vector <bool> digits;
	digits.resize(10);
	for (int i = 0; i < tests; i++)
	{
		for (int j = 0; j <= 10; j++)
			digits[j] = 0;
		cin >> number;
		bool ready = 0;
		int times = 0;
		for (int times = 1; times <= 100; times ++)
//		while (1)
		{
//			times ++
			int tmp = number*times;
			while (tmp != 0)
			{
				digits[tmp % 10] = 1;
				cerr << "seen " << tmp % 10 << "\n";
				tmp = tmp / 10;
			}
    			if (	digits[0] &&
	    			digits[1] &&
	    			digits[2] &&
	    			digits[3] &&
	    			digits[4] &&
	    			digits[5] &&
	    			digits[6] &&
	    			digits[7] &&
	    			digits[8] &&
	    			digits[9])
	    		{	
				cout << "Case #" << i+1 <<": " << number * times <<"\n";
				ready = 1;
				break;
			}
		}
		if (!ready)
			cout << "Case #" << i + 1 <<": INSOMNIA\n";

	}
}