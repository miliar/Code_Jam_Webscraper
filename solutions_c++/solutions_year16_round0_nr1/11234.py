#include <iostream>
#include <stdio.h> 

using namespace std;

int progress(int digits_arr[], int length)
{
	int count_got = 0;

	for ( int i = 0; i < length; i++ )
	{
		if (digits_arr[i] == 1)
			count_got++;
	}

	return count_got; 
}

int solve(int all_digits[], int length, int num)
{
	int counter = 1; 
	bool asleep = false; 

	while ( asleep != true )
	{
		int value = num * counter; // multiple by N 
		int change_val = value; 
		int digits = log10((float)value) + 1; // number of digits 

		for ( int j = digits - 1; j >= 0; j-- ) 
		{
			int divisor = pow((float)10, j); 
			int dig = change_val / divisor; 

			change_val -= dig * divisor; 

			all_digits[dig] = 1; 
		}

		int digits_got = progress(all_digits,10); // check amount of digits gotten 

		if (digits_got == 10)
		{
			return value; 
		}
		else
		{
			counter++; // increment counter 

			if (counter == 100)
				return 0; 
		}

	}

	return 0; 

}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output_file_large.out","w",stdout);

	int the_input;
	
	cin >> the_input; 

	for ( int i = 0; i < the_input; i++ ) // loop through all inputs 
	{
		int digits [10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }; // all digits

		int n;
		cin >> n;

		if ( n == 0 )
		{
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl; 

		}
		else
		{
			int last_num = solve(digits,10,n); 

			if (last_num == 0)
			{
				cout << "Case #" << i + 1 << ": INSOMNIA" << endl; 
			}
			else
			{
				cout << "Case #" << i + 1 << ": " << last_num << endl; 

			}
		}

	}

	return 0;
}