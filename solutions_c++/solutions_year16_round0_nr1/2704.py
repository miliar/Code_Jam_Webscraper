

#include <iostream>

using namespace std;

//Returns the number of new digits found.
int checkDigits(int64_t number, bool digitFlags[])
{
	int foundCount = 0;
	while (number)
	{
		int r = number % 10;
		number = number / 10;
		if (digitFlags[r] == 0)
		{
			foundCount++;
			digitFlags[r] = 1;
		}
	}

	return foundCount;
}


int main()
{
    
	int tCount;
	int64_t n;
	cin >> tCount;  // read t. cin knows that t is an int, so it reads it as such.
	

	for (int t = 1; t <= tCount; ++t)
	{
		cin >> n;

		if(n == 0)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
		{ 	
			int found = 0;
			bool digitFlags[10] = { 0 };
			int count = 0;

			int64_t current = 0;
			while (found < 10)
			{
				current += n;
				found += checkDigits(current, digitFlags);
				count++;
			}

			cout << "Case #" << t << ": " << current << endl;
		}

	}
}


