#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

double get_best_time(double farm_price, double farm_production, double needed_cookies);

int main()
{
	ifstream input_file("B-small.in");
	ofstream output_file("B-small.out");
	string line;
	int i = 1;
	getline(input_file, line);
	while (getline(input_file, line))
	{
		istringstream iss(line);
		double n1,n2,n3;
		iss>> n1 >> n2 >> n3;
		output_file << "Case #" <<  i <<  ": " << setprecision (7) << fixed << get_best_time(n1, n2, n3) << "\n";
		i++;
	}
	output_file.close();
	input_file.close();
	return 0;
}

double get_best_time(double farm_price, double farm_production, double needed_cookies)
{
	double current_cookies, time_spent;
	current_cookies = time_spent = 0.0;
	double production_rate = 2.0;

	while (current_cookies < needed_cookies)
	{
		if (needed_cookies/production_rate < (farm_price/production_rate + needed_cookies/(production_rate+farm_production)))
		{
			time_spent += (needed_cookies/production_rate);
			current_cookies += needed_cookies;
		}
		else if (current_cookies < farm_price )
		{
			time_spent += farm_price/production_rate;
			production_rate += farm_production;
		}
		else 
		{
			time_spent = (farm_price/production_rate + needed_cookies/(production_rate+farm_production));
			current_cookies -= farm_price;
		}
	}
	return time_spent;
}