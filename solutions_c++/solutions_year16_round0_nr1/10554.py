#include <iostream>

#define ITERATIONS 10000

using namespace std;

void reset_digits(bool *digits)
{
	for(int i = 0; i < 10; i++)
	{
		digits[i] = false;
	}
}

bool is_valid(bool *digits)
{
	for(int i = 0; i < 10; i++)
	{
		if(!digits[i])
		{
			return false;
		}
	}
	
	return true;
}

int main(int argc, char **argv)
{
	int t;
	long n;
	bool digits[10];
	reset_digits(digits);
	
	cin >> t;
	
	for(int i = 0; i < t; i++)
	{
		cin >> n;
		
		cout << "Case #" << i+1 << ": ";
		
		for(int j = 0; j <= ITERATIONS; j++)
		{
			long long copy = n * (j+1);
			
			while(copy > 0)
			{
				digits[copy%10] = true;
				copy /= 10;
			}
			
			if(is_valid(digits))
			{
				cout << n * (j+1);
				break;
			}
		}
		
		if(!is_valid(digits))
		{
			cout << "INSOMNIA";
		}
		
		cout << endl;
		
		reset_digits(digits);
	}
	
	return 0;
}
