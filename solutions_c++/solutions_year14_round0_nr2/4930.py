#include "stdafx.h"

#include <array>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

template<typename T>
T getline ( std::ifstream& inFile ) {
	T line;
	inFile >> line;
	return line;
}

std::string getline<> ( std::ifstream& inFile ) {
	std::string line;
	getline (inFile, line);
	return line;
}


int main()
{
	std::string const file_name ("D:/Downloads/B-small-attempt0");
	std::ifstream inFile (file_name+".in");
	if (!inFile.is_open())
		return 0;

	std::ofstream outFile (file_name+".out");
	if (!outFile.is_open())
		return 0;

	auto round = []( double const value ) {
		return floor( value*10E7 + 0.5 )/10E7;
	};

	int const T = getline<int> (inFile); // number of test cases

	// Iterate cases
	for ( int n = 0; n < T; n++ )
	{
		// Inputs
		auto const C = getline<double> (inFile); // cookies to buy a cookie farm
		auto const F = getline<double> (inFile); // extra cookies/sec
		auto const X = getline<double> (inFile); // cookies to win

		// Initial values
		double cookies = 0; // cookies
		double prod_rate = 2; // cookies/sec
		double spent_time = 0;

		while(true)
		{
			auto const time_to_buy_farm = round(C/prod_rate);
			auto const time_to_buy_farm_and_then_win = time_to_buy_farm+round(X/(prod_rate+F));
			auto const time_to_win = round(X/prod_rate);

			if ( time_to_buy_farm_and_then_win < time_to_win )
			{
				// Buy a farm!
				spent_time += time_to_buy_farm;
				// increase total cookie production
				prod_rate += F;
			}
			else
			{
				// Wait until you have X cookies!
				spent_time += time_to_win;
				break;
			}
		}

		// print result
		outFile << "Case #" << n+1 << ": ";
		outFile.precision(7);
		outFile << std::fixed << spent_time;
		outFile << '\n';
	}
		
	inFile.close();
	outFile.close();


	return 0;
}

