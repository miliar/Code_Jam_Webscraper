#include <cmath>
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

bool is_Pal ( string number )
{
	if ( number.size() == 1 )
		return true;

	unsigned int left_ptr = 0;
	unsigned int right_ptr = number.size() - 1;

	while ( left_ptr <= right_ptr ){
		if ( number[left_ptr] != number[right_ptr] )
			return false;
		++left_ptr;
		--right_ptr;
	}

	return true;
}

double ret_Square ( int number )
{
	double cpy = number;
	double sqrt_cpy = sqrt(cpy);

	if ( fmod ( sqrt_cpy, floor(sqrt_cpy) ) != 0 )
		return -1;
	return sqrt_cpy;
}

int solve_Case ()
{
	int successes = 0;
	string number, number1;
	
	int lower_B , upper_B;
	cin >> lower_B >> upper_B;
	double result = 0.0;

	for ( lower_B; lower_B <= upper_B; ++lower_B ) {
		result = ret_Square(lower_B);
		if ( result != -1 ) {	
			stringstream a;
			a << lower_B;
                        a >> number;
			
			if ( is_Pal(number) ){
				stringstream b;
				b << result;	
				b >> number1;
				if ( is_Pal(number1) ){
					++successes;
				}
			}
		}
	} 
	return successes;
}



int main ()
{
	int num_Cases;
	vector <int> results;
	cin >> num_Cases;

	for ( unsigned int i = 0; i < num_Cases; ++i ) 
		results.push_back( solve_Case() );

	for ( unsigned int i = 0; i < results.size(); ++i ) 
		cout << "Case #" << i+1 << ": " << results[i] << endl;
	return 0;
}
