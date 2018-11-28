#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

typedef unsigned long long int input_num_t;

input_num_t reverse (input_num_t n)
{
	input_num_t temp = 0;
	while (n != 0)
	{
		temp *= 10;
		temp += n%10;
		n = n/10;
	}

	return temp;
}


bool is_palindrome (input_num_t num)
{
	return (num == reverse (num));
}

vector <input_num_t> palindrom_squares;


void calc_palindrome_squares (input_num_t max)
{
	int num = 2;
	int prev_square = 1;
	int current_square = prev_square + (num-1) + (num-1) + 1;
	palindrom_squares.push_back (1);

	while (current_square <= max)
	{
		if (is_palindrome (num) && is_palindrome (current_square))
		{
			palindrom_squares.push_back (current_square);
		}

		++num;
		prev_square = current_square;
		current_square = prev_square + (num-1) + (num-1) + 1;
	}
}


int main ()
{
	// For small data set
	calc_palindrome_squares (1e14);

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; ++i)
	{
	    input_num_t min, max;
		cin >> min >> max;

		int n_palindrom_squares = 0;

		int k = 0;
		while (k < palindrom_squares.size () && palindrom_squares[k] < min) ++k;



		while (k < palindrom_squares.size () && palindrom_squares[k] <= max)
		{
			++n_palindrom_squares;
			++k;
		}

		cout << "Case #" << i+1 << ": " << n_palindrom_squares << endl;
	}

	return 0;
}