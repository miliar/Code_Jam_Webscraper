#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int test_cases = 0;

	ifstream i_file;
	i_file.open("input.txt");
	i_file >> test_cases; 
	
	ofstream o_file;
	o_file.open("output.txt");


	long double cookie_rate = 2.0;
	
	long double factory_price = 0.0;
	long double cookie_bonus = 0.0;
	long double cookie_goal = 0.0;
	long double total_time = 0.0;	

	long double current_time_to_finish = 0.0;
	int factories_owned = 0;

	bool finished = false;
	
	for (int i=0; i<test_cases; i++)
	{
		cookie_rate = 2.0;
		i_file >> factory_price;
		i_file >> cookie_bonus;
		i_file >> cookie_goal;
		total_time = 0.0;

		factories_owned = 0;
		finished = false;

		while (!finished)
		{
			current_time_to_finish = cookie_goal / cookie_rate;

			if (current_time_to_finish > (factory_price/(cookie_rate) + (cookie_goal / (cookie_rate + cookie_bonus)))) 
			{	
				factories_owned++;
				total_time = total_time + (factory_price/(cookie_rate));
				cookie_rate += cookie_bonus;
			}
			else
			{
				total_time = total_time + current_time_to_finish;
				finished = true;
			}
		}
		o_file.precision(7);
		o_file << "Case #" << i + 1 << ": " << fixed << total_time << endl;

	}

}