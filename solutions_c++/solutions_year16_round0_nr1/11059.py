#include <iostream>
#include <vector>
#include <algorithm>    // std::find
#include <fstream>
#include <string>

using namespace std;
vector<int> seen_sheep_digits_tracker (10,0) ;

vector<int> seperate_into_digits( unsigned long long int value )
{
    vector<int> digits ;
    for( ; value > 0 ; value /= 10 ) digits.push_back( value%10 ) ;
    reverse( digits.begin(), digits.end() ) ;
    return digits ;
}

void RunInstances()
{
	int N;
	cin >> N;

    unsigned long long int next_number = 0;

	if (N == 0)
	{
		cout << "INSOMNIA";
		return;
	}


	bool saw_all_numbers = false;

	vector <int> temp_number;
	// this can be changed to a for loop, limit for i is k * 10
	while (!saw_all_numbers)
	{
		next_number = next_number + N;
		temp_number = seperate_into_digits(next_number);
		//cout << "Next number = " << next_number << endl;

		for (int j = 0 ; j < 10 ; ++j )
		{
			if (seen_sheep_digits_tracker[j] == 0 )
			{
				vector<int>::iterator unseendigit_inTempNumber = find(temp_number.begin(), temp_number.end(), j) ;
				if(unseendigit_inTempNumber == temp_number.end()) {

				}
				else
				{
					seen_sheep_digits_tracker[j] = 1;
				}
			}
		}

		// Test if all digits were seen
		vector<int>::iterator unseendigit = find(seen_sheep_digits_tracker.begin(), seen_sheep_digits_tracker.end(),0) ;
		if(unseendigit == seen_sheep_digits_tracker.end()) {
			cout << next_number;
			saw_all_numbers = true;

		}
	}

	return;
}

int main()
{
    int number_of_cases;
    cin >> number_of_cases;


    for (int i = 1; i <= number_of_cases; ++i)
    {
        cout << "Case #" << i << ": " ;
        RunInstances();
        fill(seen_sheep_digits_tracker.begin(), seen_sheep_digits_tracker.end(), 0);
        cout << endl;
    }
}
